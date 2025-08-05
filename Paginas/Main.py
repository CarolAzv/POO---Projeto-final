import streamlit as st
from Paginas.UsuarioPage import show as show_usuario
from Modelos.Entidades.Usuario import Usuario
from Modelos.Persistencia.Usuarios import Usuarios

if "pagina_atual" not in st.session_state:
    st.session_state.pagina_atual = "Menu"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.object_usuario = None

def main():
    if st.session_state.logged_in:
        show_usuario()
        return
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
            with st.form("login_usuario_form"):
                email = st.text_input("E-mail:", key="login_email_input")
                senha = st.text_input("Senha:", type="password", key="login_senha_input")

                submitted = st.form_submit_button("Entrar")

                if submitted:
                    if not email or not senha:
                        st.error("Por favor, preencha todos os campos.")
                    else:
                        try:
                            tipo_usuario_logado, obj_usuario = Usuario.login(email, senha)

                            st.session_state.logged_in = True
                            st.session_state.tipo_usuario = tipo_usuario_logado
                            st.session_state.object_usuario = obj_usuario

                            st.success(f"Login bem-sucedido como {tipo_usuario_logado.capitalize()}!")

                            st.session_state.pagina_atual = "UsuarioPage"

                            st.rerun() 

                        except ValueError as e:
                            st.error(f"Erro no login: {e}")
                        except Exception as e:
                            st.error(f"Ocorreu um erro inesperado: {e}")


        if st.session_state.pagina_atual =="Cadastro":
            st.title("Você está fazendo o cadastro!")
            st.write("Preencha os dados para criar sua conta.")

            novo_nome = st.text_input("Nome Completo:", key="cadastro_nome")
            novo_email = st.text_input("Email:", key="cadastro_email")
            novo_cell = st.text_input("Numero de Celular:", key="cadastro_cell")
            novo_senha = st.text_input("Senha:", key="cadastro_senha")

            if st.button("Cadastrar", key="btn_cadastrar"):
                if not novo_nome or not novo_email or not novo_cell or not novo_senha:
                    st.error("Preencha todos os campos para concluir o cadastro.")
                else:
                    try:
                        novo_usuario = Usuario(id=0, nome=novo_nome, email=novo_email, fone=novo_cell, senha = novo_senha)
                        Usuarios.inserir(novo_usuario)

                        st.success("Cadastro realizado com sucesso!")
                        st.session_state.pagina_atual = 'login'
                        st.rerun()
                    except ValueError as e:
                        st.error(f"Erro no cadastro: {e}")
                    except Exception as e:
                        st.error(f"Ocorreu um erro inesperado: {e}")

main()
