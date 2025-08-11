import streamlit as st
import pandas as pd
from Modelos.Entidades.Usuario import Usuario
from Modelos.Persistencia.Usuarios import Usuarios
from Modelos.Entidades.Membro import Membro
from Modelos.Persistencia.Membros import Membros
from Modelos.Entidades.Papel import Papel
from Modelos.Persistencia.Papeis import Papeis
from Modelos.Entidades.Projeto import Projeto
from Modelos.Persistencia.Projetos import Projetos
from Modelos.Entidades.Tarefa import Tarefa
from Modelos.Persistencia.Tarefas import Tarefas
from datetime import datetime

def show():
    st.title("Espaço do Usuario")
    usuario_obj = st.session_state.get('object_usuario')
    col_esquerda,col_centro,col_direita = st.columns([1,1,0.2])
    with col_esquerda:
        st.write("Bem-vindo(a), usuario")
    with col_direita:
        if st.button("Sair",key = "logout_usuario_page"):
            st.session_state.logged_in = False
            st.session_state.tipo_usuario = None
            st.session_state.object_usuario = None

            st.session_state.pagina_atual = "Menu"
            st.success("Você foi desconectado com sucesso")
            st.rerun()

    
    tab_projetos,tab_tarefas,tab_atualizarUsuario = st.tabs([
        "Ver seus Projetos",
        "Ver suas Tarefas",
        "Atualizar dados do Usuario",
    ])

    #=======================================================================================================================
    #=======================================================================================================================
    #=======================================================================================================================
    with tab_projetos:
        st.header("Ver seus Projetos")
        opcoes_projeto = st.radio(
            "Selecione uma ação:",
            ("Criar Projeto","Listar Projetos","Ver Projeto","Adicionar Membro","Excluir Membro"),
            key = "radio_clientes"
        )
        if opcoes_projeto == "Criar Projeto":
            st.subheader("Criar novo Projeto")
            st.write("Preencha tudo para criar um novo projeto.")
            with st.form("form_cadastro_projeto", clear_on_submit=True):
                novo_nome = st.text_input("Nome:", key="projeto_nome")
                novo_descricao = st.text_input("Descrição:", key="projeto_descricao")
                submitted_projeto = st.form_submit_button("Criar Projeto")

                if submitted_projeto:
                    if not novo_nome or not novo_descricao:
                        st.error("Por favor, preencha todos os campos.")
                    else:
                        try:
                            #                            v- check if this is right                                                                                           v- check if this is right 
                            novo_projeto = Projeto(id=0, idCriador=1, nome=novo_nome, descricao=novo_descricao, data_comeco=datetime.now(), data_fim = 0)
                            Projetos.inserir(novo_projeto)
                            
                            st.success(f"Projeto '{novo_nome}' criado com sucesso!")
                            
                        except ValueError as e:
                            st.error(f"Erro na criação: {e}")
                        except Exception as e:
                            st.error(f"Ocorreu um erro inesperado: {e}")

        elif opcoes_projeto == "Listar Projetos":
            st.subheader("Lista de Projetos")
            todos_projetos = Projetos.listar()
            if todos_projetos:
                dados_projetos = [c.to_dict() for c in todos_projetos]
                
                df_projetos = pd.DataFrame(dados_projetos) 
                
                st.dataframe(df_projetos) 
            else:
                st.info("Nenhum projeto criado ainda.")

        elif opcoes_projeto == "Ver Projeto":
            st.subheader("Projeto")
            projento_vendo = None
            st.write("Indique o nome ou id do projeto: ")
            with st.form("form_ver_projeto", clear_on_submit=True):
                proj_nome = st.text_input("Nome do projeto:", key="projeto_nome")
                proj_id = st.text_input("Id do projeto:", key="projeto_id")
                submitted_ver_proj = st.form_submit_button("Visualizar")

                if submitted_ver_proj:
                     if not novo_nome and not novo_descricao:
                        st.error("Por favor, preencha pelo menos um dos campos.")
                else:
                    projento_vendo = [proj_nome, proj_id]
                
            todos_projetos = Projetos.listar()
            if todos_projetos:
                for i, projeto in todos_projetos:
                    if projento_vendo[0] == projeto.get_nome or projento_vendo[1] == projeto.get_id:
                        st.write(f"**Id:** {projeto.get_id()}")
                        st.write(f"**Nome:** {projeto.get_nome()}")
                        st.write(f"**Descrição:** {projeto.get_descricao()}")
                        st.write(f"**Data de inicio:** R$ {projeto.get_data_comeco().strftime('%d/%m/%Y %H:%M')}")
                        st.write(f"**Data de finalização:** {projeto.get_data_fim().strftime('%d/%m/%Y %H:%M')}")
                        st.divider()
                        todos_membros = Membros.listar()
                        if not todos_membros:
                            st.write("Nenhuma membro criado.")
                        else:
                            for i, membro in todos_membros:
                                if projento_vendo[1] == membro.get_idProjeto:
                                    st.write(f"**Id:** {membro.get_id()}")
                                    st.write(f"**Id do Membro:** {membro.get_idUsuario()}")

                        todos_tarefas = Tarefas.listar()
                        if not todos_tarefas:
                            st.write("Nenhuma tarefa nesse projeto.")
                        else:
                            for i, tarefa in todos_tarefas:
                                if projento_vendo[1] == tarefa.get_idProjeto:
                                    st.write(f"**Id:** {tarefa.get_id()}")
                                    st.write(f"**Id do Membro:** {tarefa.get_idUsuario()}")
                                    st.write(f"**Descrição:** {tarefa.get_descriçao()}")
                                    st.write(f"**Data de inicio:** R$ {tarefa.get_data_comeco().strftime('%d/%m/%Y %H:%M')}")
                                    st.write(f"**Status:** {tarefa.get_get_status()}")

            else:
                st.info("Nenhum projeto criado ainda.")

        elif opcoes_projeto == "Adicionar Membro":
            st.subheader("Adicionar Membro a um Projeto")
            todos_projetos = Projetos.listar()
            with st.form("form_adi_membro", clear_on_submit=True):
                proj_id = st.text_input("Id do projeto:", key="projeto_id")
                membro_id = st.text_input("Id do Usuario:", key="projeto_id")
                submitted_p = st.form_submit_button("Adicionar Membro")

                if submitted_p:
                     if not novo_nome and not novo_descricao:
                        st.error("Por favor, preencha pelo menos um dos campos.")
                else:
                    try:
                        novo_membro = Membro(id=0, idUsuario=membro_id, idProjeto=proj_id)
                        Membros.inserir(novo_membro)

                        st.success("Membro adicionado com sucesso!")
                    except ValueError as e:
                        st.error(f"Erro ao adicionar: {e}")
                    except Exception as e:
                        st.error(f"Ocorreu um erro inesperado: {e}")

        elif opcoes_projeto == "Excluir Membro":
            st.subheader("Excluir Membro")
            todos_projetos = Projetos.listar()
            todos_membros = Membros.listar()
            nossos_projetos = Projetos.filtrar(todos_projetos, 1)
            nossos_membros = Projetos.filtrar(todos_membros, nossos_projetos)
            
            opcoes_membros_selectbox = [f"{c.get_nome()} (ID: {c.get_id()})" for c in todos_membros]
            cliente_selecionado_str = st.selectbox(
                "Selecione o cliente para excluir:",
                opcoes_membros_selectbox,
                key="select_cliente_delete"
            )
            cliente_id_str = cliente_selecionado_str
            cliente_id = cliente_id_str
            cliente_para_excluir = Usuarios.listar_id(cliente_id)

            if cliente_para_excluir:
                st.warning(f"Tem certeza que deseja excluir o cliente: '{cliente_para_excluir.get_nome()}' (ID: {cliente_para_excluir.get_id()})?")
                if st.button("Confirmar Exclusão", key="confirm_delete_cliente"):
                    try:
                        Usuario.excluir(cliente_para_excluir) 
                        st.success(f"Cliente '{cliente_para_excluir.get_nome()}' excluído com sucesso!")
                        st.rerun() 
                    except ValueError as e:
                        st.error(f"Erro na exclusão: {e}")
                    except Exception as e:
                        st.error(f"Ocorreu um erro inesperado: {e}")
            else:
                st.warning("Cliente selecionado não encontrado.")
        
    #=======================================================================================================================
    #=======================================================================================================================
    #=======================================================================================================================
    with tab_tarefas:
        st.header("Ver suas Tarefas")
        opcoes_tarefas = st.radio(
            "Selecione uma opção",
            ("Listar suas tarefas","Atualizar suas tarefas"),
            key = "radio_entregadores"
        )

    #=======================================================================================================================
    #=======================================================================================================================
    #=======================================================================================================================
    with tab_atualizarUsuario:
        st.header("Atualizar dados do Usuario")
        
        with st.form("form_atualizar_usuario", clear_on_submit=False):
            nome_atualizado = st.text_input("Nome do Usuário:", key="nome_usuario_update")
            email_atualizado = st.text_input("Email:", key="email_usuario_update")
            cell_atualizado = st.text_input("Celular:", key="cell_usuario_update")
            senha_atualizada = st.text_input("Senha:", key="senha_usuario_update", type="password")
            submit_atualizacao = st.form_submit_button("Atualizar Usuario")

            if submit_atualizacao:
                if not nome_atualizado or not email_atualizado or not cell_atualizado or not senha_atualizada:
                    st.error("Por favor, preencha todos os campos para atualização.")
                else:
                    try:
                        usuario_atualizado = Usuario(
                            1,
                            nome_atualizado,
                            email_atualizado,
                            cell_atualizado,
                            senha_atualizada
                        )
                        Usuarios.atualizar(usuario_atualizado) 
                        st.success(f"Usuario '{nome_atualizado}' atualizada com sucesso!")
                        st.rerun()
                    except ValueError as e:
                        st.error(f"Erro na atualização: {e}")
                    except Exception as e:
                        st.error(f"Ocorreu um erro inesperado: {e}")
