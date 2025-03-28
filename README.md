# WhatsApp Automation Bot

Este repositório contém um aplicativo desenvolvido para automatizar o envio de mensagens no WhatsApp Web a partir de uma planilha de contatos. O projeto foi desenvolvido utilizando HTML, CSS, JavaScript e Python (Selenium) para interação com o WhatsApp Web.

## Funcionalidades

- **Envio Automático de Mensagens:** Permite o envio de mensagens personalizadas para uma lista de contatos extraída de uma planilha.
- **Interface Amigável:** Design responsivo e intuitivo para fácil interação.
- **Lista de Contatos Salvos:** Registra contatos que não puderam ser enviados para tentativa futura.
- **Personalização de Mensagens:** Permite definir uma mensagem padrão a ser enviada para todos os contatos.
- **Animação de Carregamento:** Exibe um loader animado enquanto a automação está em execução.
- **Compatibilidade Desktop:** Interface otimizada para uso em computadores.

## Tecnologias Utilizadas

- **Frontend:** HTML, CSS e JavaScript
- **Backend:** Python com Selenium
- **Bibliotecas Utilizadas:**
  - `Selenium` para automação do WhatsApp Web
  - `pandas` para manipulação de planilhas

## Como Funciona

1. **Upload da Planilha:** O usuário carrega um arquivo `.xlsx` contendo os números de telefone e mensagens.
2. **Configuração da Mensagem:** É possível definir uma mensagem padrão que será aplicada aos contatos.
3. **Início da Automção:** O bot abre o WhatsApp Web, aguarda 30 segundos para carregamento e começa o envio.
4. **Feedback Visual:** Durante o envio, uma animação de carregamento é exibida.
5. **Registro de Falhas:** Caso algum contato não possa ser enviado, ele é salvo em uma lista para reenvio futuro.

## Como Executar

### Requisitos

- Python 3 instalado
- Google Chrome instalado
- WebDriver compatível com sua versão do Chrome (coloque o `chromedriver` na pasta do projeto)

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/whatsapp-automation-bot.git
   cd whatsapp-automation-bot
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o script Python:
   ```bash
   python bot.py
   ```
4. Abra o arquivo `index.html` no navegador para acessar a interface.

## Estrutura do Projeto

```
whatsapp-automation-bot/
│-- bot.py                 # Script principal do bot
│-- requirements.txt       # Dependências do projeto
│-- static/
│   ├── styles.css        # Estilos CSS
│   ├── script.js         # Scripts JavaScript
│-- templates/
│   ├── index.html       # Interface principal
│-- README.md             # Documentação do projeto
```

## Considerações Finais

Este projeto foi desenvolvido para facilitar o envio automatizado de mensagens pelo WhatsApp Web de forma simples e eficiente. Para melhorias ou sugestões, sinta-se à vontade para contribuir! 🚀
