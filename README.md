📇 Agenda de Contatos com Google Sheets + Streamlit
Olá! Seja bem-vindo(a) ao meu projeto de Agenda de Contatos! 👋
Aqui você encontra um exemplo simples, mas super funcional, de como usar o Google Sheets como banco de dados para salvar seus contatos, e exibir tudo com um app web feito em Streamlit — prático, leve e fácil de usar.

🚀 O que este projeto faz?
Salva contatos (nome e email) diretamente numa planilha do Google Sheets.

Lista os contatos cadastrados na mesma planilha.

Evita duplicatas para manter tudo organizadinho.

Interface amigável e simples, para você adicionar e ver seus contatos rapidinho.

⚙️ Como funciona?
Você preenche o formulário com o nome e email.

Ao clicar em "Salvar", o app envia esses dados para a sua planilha no Google Sheets.

O app mostra todos os contatos já cadastrados.

Tudo isso usando a magia do Google Sheets API + Streamlit.

🧑‍💻 Como usar?
Clone este repositório.

Crie um projeto no Google Cloud e ative as APIs do Google Sheets e Google Drive.

Gere uma conta de serviço e baixe as credenciais JSON.

Configure a variável de ambiente GOOGLE_SHEETS_CREDENTIALS_JSON no Streamlit Community Cloud (ou salve o arquivo credentials.json localmente).

Crie uma planilha chamada basecontatos e compartilhe com o e-mail da sua conta de serviço.

Rode o app:

bash
Copiar
Editar
