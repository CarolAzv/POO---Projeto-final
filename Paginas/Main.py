import streamlit as st
from Modelos.Entidades.Usuario import Usuario
from Modelos.Persistencia.Usuarios import Usuarios

if "pagina_atual" not in st.session_state:
    st.session_state.pagina_atual = "Menu"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.object_usuario = None

def main():
    if st.session_state.logged_in:
        st.title("testando")
    else:
        if st.session_state.pagina_atual =="Menu":
            st.title("isso deveria aparecer")
        if st.session_state.pagina_atual =="Login":
            st.title("Você está fazendo o Login!")
        if st.session_state.pagina_atual =="Cadastro":
            st.title("Você está fazendo o Cadasro!")
