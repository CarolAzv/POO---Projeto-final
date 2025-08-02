import streamlit as st

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
            st.title("Organização e Destrubuição de Projetos e Tarefas")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Entrar", key="btn_entrar_home"):
                    st.session_state.pagina_atual = "Login"
                    st.rerun()
            with col2:
                if st.button("Cadastre-se", key="btn_cadastro_home"):
                    st.session_state.pagina_atual = "Cadastro"
                    st.rerun()
        if st.session_state.pagina_atual =="Login":
            st.title("Você está fazendo o Login!")
        if st.session_state.pagina_atual =="Cadastro":
            st.title("Você está fazendo o cadastro!")

main()
