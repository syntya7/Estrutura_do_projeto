import streamlit as st
from gsheets import add_contato, listar_contatos

st.set_page_config(page_title="Agenda", layout="centered")
st.title("📇 Exemplo de Agenda de Contatos (Google Sheets)")

with st.form("form_contato"):
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    enviar = st.form_submit_button("Salvar")

    if enviar:
        if nome and email:
            sucesso = add_contato(nome, email)
            if sucesso:
                st.success("Contato salvo com sucesso!")
            else:
                st.warning("Contato já existe na lista.")
        else:
            st.warning("Preencha todos os campos.")

st.subheader("📋 Contatos cadastrados")

dados = listar_contatos()

st.write("DEBUG - Dados retornados:", dados)  # Linha para depuração, remova depois

if dados:
    try:
        for contato in dados:
            nome = contato.get("nome", "Sem nome")
            email = contato.get("email", "Sem email")
            st.write(f"**{nome}** - {email}")
    except Exception as e:
        st.error(f"Erro ao renderizar contatos: {e}")
else:
    st.info("Nenhum contato cadastrado.")
