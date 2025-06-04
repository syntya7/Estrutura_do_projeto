import streamlit as st
from gsheets import add_contato, listar_contatos

st.set_page_config(page_title="Agenda", layout="centered")
st.title("📇 Cadastro dos associados")

with st.form("form_contato"):
    id_assoc = st.text_input("Digite o id da associação")
    nome = st.text_input("Nome")
    endereco = st.text_input("Digite seu endereço")
    telefone = st.text_input("Digite seu telefone") 
    enviar = st.form_submit_button("Salvar")

    if enviar:
        if nome and id_assoc and endereco and telefone:
            sucesso = add_contato(nome, id_assoc, endereco, telefone)
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
            id_assoc = contato.get("id_assoc", "Sem assoc")
            telefone = contato.get("telefone", "Sem telefone")
            endereco = contato.get("endereco", "Sem endereco")
           
            st.write(f"**{nome}** - {id_assoc} - {telefone} - {endereco}")
    except Exception as e:
        st.error(f"Erro ao renderizar contatos: {e}")
else:
    st.info("Nenhum contato cadastrado.")
