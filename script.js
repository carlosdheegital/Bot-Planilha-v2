document.getElementById('formMensagem').addEventListener('submit', function(event) {
    document.getElementById('loading').classList.remove('hidden');
    document.querySelector('.btn').disabled = true;
});

document.getElementById('uploadForm').addEventListener('submit', function(event) {
    document.getElementById('loading').classList.remove('hidden');
    document.querySelector('.btn').disabled = true;
});

document.getElementById('toggleFailList').addEventListener('click', function() {
    const failList = document.getElementById('failList');
    failList.classList.toggle('hidden');
});

document.getElementById('formMensagem').addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o envio do formulário de forma padrão

    // Exibe o loader e oculta o botão
    document.getElementById('submitBtn').style.display = 'none';
    document.getElementById('loaderContainer').classList.remove('hidden');

    // Simula o processo de envio
    setTimeout(() => {
        // Aqui você pode adicionar a lógica para enviar o formulário via Ajax, por exemplo

        // Depois de "enviado", esconde o loader e exibe o botão novamente
        document.getElementById('loaderContainer').classList.add('hidden');
        document.getElementById('submitBtn').style.display = 'inline-block';

        // Você pode adicionar algum feedback aqui, como uma mensagem de sucesso
        alert("Mensagem enviada com sucesso!");
    }, 3000); // Simulando 3 segundos de envio
});
