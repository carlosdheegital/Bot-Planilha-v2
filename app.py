from flask import Flask, render_template, request, jsonify
import pandas as pd
import openpyxl
import pyautogui
import webbrowser
from urllib.parse import quote
import time
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def processar_planilha(file):
    """Processa a planilha enviada e verifica se possui as colunas necessárias."""
    try:
        ext = file.filename.split('.')[-1].lower()
        if ext == 'csv':
            dados = pd.read_csv(file)
        elif ext in ['xls', 'xlsx']:
            dados = pd.read_excel(file)
        else:
            return None, "Formato inválido. Envie um arquivo CSV ou Excel."

        colunas_necessarias = {'NOME', 'TELEFONE', 'DATA'}
        if not colunas_necessarias.issubset(dados.columns):
            return None, "A planilha precisa ter as colunas: NOME, TELEFONE, DATA."
        
        return dados, None
    except Exception as e:
        return None, f"Erro ao processar o arquivo: {e}"

def enviar_mensagem_via_whatsapp(nome, telefone, vencimento):
    """Envia mensagens via WhatsApp Web."""
    try:
        mensagem = f'Olá {nome}, seu boleto vence no dia {vencimento.strftime("%d/%m/%Y")}. Qualquer dúvida, estou à disposição.'
        url = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
        
        webbrowser.open(url)
        time.sleep(15)  # Tempo para carregar a página
        
        pyautogui.press('enter')  # Pressiona Enter para enviar a mensagem
        time.sleep(5)  
        pyautogui.hotkey('ctrl', 'w')  # Fecha a aba do WhatsApp
    except Exception as e:
        with open('erros.csv', 'a', newline='', encoding='utf-8') as arquivo:
            arquivo.write(f'{nome},{telefone},{vencimento}\n')

@app.route('/')
def index():
    """Renderiza a página inicial."""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_planilha():
    """Recebe um arquivo de planilha e envia mensagens para os contatos listados."""
    file = request.files.get('file')
    if not file or file.filename == '':
        return jsonify({"status": "erro", "mensagem": "Nenhum arquivo enviado."})
    
    dados, erro = processar_planilha(file)
    if erro:
        return jsonify({"status": "erro", "mensagem": erro})
    
    time.sleep(10)  # Tempo para garantir que o WhatsApp Web carregue completamente
    
    for _, row in dados.iterrows():
        enviar_mensagem_via_whatsapp(row['NOME'], row['TELEFONE'], pd.to_datetime(row['DATA']))
    
    return jsonify({"status": "sucesso", "mensagem": "Mensagens enviadas com sucesso!"})

@app.route('/enviar', methods=['POST'])
def enviar_manual():
    """Recebe dados de um único contato e envia a mensagem via WhatsApp."""
    dados = request.get_json()
    if not all(k in dados for k in ['nome', 'numero', 'data']):
        return jsonify({"status": "erro", "mensagem": "Todos os campos são obrigatórios."})
    
    enviar_mensagem_via_whatsapp(dados['nome'], dados['numero'], pd.to_datetime(dados['data']))
    return jsonify({"status": "sucesso", "mensagem": "Mensagem enviada com sucesso!"})

if __name__ == '__main__':
    # Abre o navegador automaticamente quando o servidor iniciar
    webbrowser.open("http://127.0.0.1:5001")
    
    # Inicia o servidor Flask
    app.run(debug=True, host="0.0.0.0", port=5001)
