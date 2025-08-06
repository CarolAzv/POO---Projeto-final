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
                            novo_projeto = Projeto(id=0, idCriador=st.session_state.object_usuario(id), nome=nome_novo, descricao=novo_descricao, data_comeco=datetime.now(), data_fim = 0)
                            Projetos.inserir(novo_projeto)
                            
                            st.success(f"Projeto '{nome_novo}' criado com sucesso!")
                            
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
            st.white("Indique o nome ou id do projeto: ")
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
                submitted_ver_proj = st.form_submit_button("Visualizar")

                if submitted_ver_proj:
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
            nossos_projetos = Projetos.filtrar(todos_projetos, st.session_state.object_usuario[id])
            nossos_membros = Projetos.filtrar(todos_membros, nossos_projetos)
            
            opcoes_membros_selectbox = [f"{c.get_nome()} (ID: {c.get_id()})" for c in todos_membros]
            cliente_selecionado_str = st.selectbox(
                "Selecione o cliente para excluir:",
                opcoes_membros_selectbox,
                key="select_cliente_delete"
            )
            cliente_id_str = cliente_selecionado_str.split('(ID: ')[1][:-1]
            cliente_id = int(cliente_id_str)
            cliente_para_excluir = Clientes.listar_id(cliente_id)

            if cliente_para_excluir:
                st.warning(f"Tem certeza que deseja excluir o cliente: '{cliente_para_excluir.get_nome()}' (ID: {cliente_para_excluir.get_id()})?")
                if st.button("Confirmar Exclusão", key="confirm_delete_cliente"):
                    try:
                        Clientes.excluir(cliente_para_excluir) 
                        st.success(f"Cliente '{cliente_para_excluir.get_nome()}' excluído com sucesso!")
                        st.rerun() 
                    except ValueError as e:
                        st.error(f"Erro na exclusão: {e}")
                    except Exception as e:
                        st.error(f"Ocorreu um erro inesperado: {e}")
            else:
                st.warning("Cliente selecionado não encontrado.")
                

        """elif opcoes_cliente == "Listar Compras": 
            st.subheader("Todas as Compras Realizadas")
            todos_pedidos = Pedidos.listar()

            if not todos_pedidos:
                st.info("Nenhuma compra realizada ainda.")
            else:
                # Ordenar os pedidos do mais recente para o mais antigo
                todos_pedidos.sort(key=lambda p: p.get_data_pedido(), reverse=True)

                for i, pedido in enumerate(todos_pedidos):
                    st.markdown(f"---") 
                    st.markdown(f"### Pedido ID: {pedido.get_id()}")
                    
                    cliente = Clientes.listar_id(pedido.get_cliente_id())
                    cliente_nome = cliente.get_nome() if cliente else "Cliente Desconhecido"
                    st.write(f"**Cliente:** {cliente_nome} (ID: {pedido.get_cliente_id()})")
                    
                    st.write(f"**Data do Pedido:** {pedido.get_data_pedido().strftime('%d/%m/%Y %H:%M')}")
                    st.write(f"**Status:** {pedido.get_status()}")
                    st.write(f"**Valor Total:** R$ {pedido.get_valor_total():.2f}")
                    st.write(f"**Endereço de Entrega:** {pedido.get_endereco()}")

                    entregador = Entregadores.listar_id(pedido.get_entregador_id()) if pedido.get_entregador_id() else None
                    entregador_nome = entregador.get_nome() if entregador else "Não Atribuído"
                     st.write(f"**Entregador:** {entregador_nome}")

                    if pedido.get_itens_pedidos():
                        st.write("**Itens do Pedido:**")
                        for item in pedido.get_itens_pedidos():
                            produto_info = Produtos.listar_id(item.get('produto_id'))
                            produto_nome = produto_info.get_nome() if produto_info else "Produto Desconhecido"
                            st.markdown(f"- **{produto_nome}** (Qtd: {item.get('quantidade')}, R$ {item.get('preco_unitario'):.2f} cada)")
                    else:
                        st.info("Nenhum item detalhado para este pedido.")"""
        
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
        if opcoes_tarefas == "Listar entregadores":
            st.subheader("Lista de Entregadores cadastrados")
            todos_entregadores = Entregadores.listar()
            if todos_entregadores:
                dados_entregadores = [c.to_dict() for c in todos_entregadores]
                
                df_entregadores = pd.DataFrame(dados_entregadores) 
                
                st.dataframe(df_entregadores) 
            else:
                st.info("Nenhum entregador cadastrado ainda.")

        elif opcoes_tarefas == "Atualizar dados do Entregador":
            st.subheader("Atualizar Dados do Entregador")
            todos_entregadores = Entregadores.listar()
            if not todos_entregadores:
                st.info("Nenhum entregador cadastrado para atualizar.")
            else:
                opcoes_entregadores_selectbox = [f"{e.get_nome()} (ID: {e.get_id()})" for e in todos_entregadores]
                entregador_selecionado_str = st.selectbox(
                    "Selecione o entregador para atualizar:",
                    opcoes_entregadores_selectbox,
                    key="select_entregador_update"
                )
                entregador_id_str = entregador_selecionado_str.split('(ID: ')[1][:-1]
                entregador_id = int(entregador_id_str)
                entregador_para_atualizar = Entregadores.listar_id(entregador_id)

                if entregador_para_atualizar:
                    with st.form("form_atualizar_entregador", clear_on_submit=False):
                        st.write(f"Atualizando entregador ID: {entregador_para_atualizar.get_id()}")
                        nome_atualizado = st.text_input("Nome Completo:", value=entregador_para_atualizar.get_nome(), key="nome_entregador_update")
                        email_atualizado = st.text_input("Email:", value=entregador_para_atualizar.get_email(), key="email_entregador_update")
                        senha_atualizada = st.text_input("Nova Senha (deixe em branco para manter a atual):", type="password", key="senha_entregador_update")
                        fone_atualizado = st.text_input("Telefone:", value=entregador_para_atualizar.get_fone(), key="fone_entregador_update")
                        transporte_atualizado = st.text_input("Transporte de Entregas:", value=entregador_para_atualizar.get_transporte(), key="transporte_entregador_update")

                        submit_atualizacao = st.form_submit_button("Atualizar Entregador")

                        if submit_atualizacao:
                            if not nome_atualizado or not email_atualizado or not fone_atualizado or not transporte_atualizado:
                                st.error("Por favor, preencha todos os campos.")
                            else:
                                try:
                                    entregador_atualizado_obj = Entregador(
                                        id=entregador_para_atualizar.get_id(),
                                        nome=nome_atualizado,
                                        email=email_atualizado,
                                        senha=senha_atualizada if senha_atualizada else entregador_para_atualizar.get_senha(),
                                        fone=fone_atualizado,
                                        transporte=transporte_atualizado
                                    )
                                    Entregadores.atualizar(entregador_atualizado_obj)
                                    st.success(f"Entregador '{nome_atualizado}' atualizado com sucesso!")
                                    st.rerun()
                                except ValueError as e:
                                    st.error(f"Erro na atualização: {e}")
                                except Exception as e:
                                    st.error(f"Ocorreu um erro inesperado: {e}")
                else:
                    st.warning("Entregador selecionado não encontrado. Por favor, selecione um entregador válido.")

    #=======================================================================================================================
    #=======================================================================================================================
    #=======================================================================================================================
    with tab_atualizarUsuario:
        st.header("Atualizar dados do Usuario")
        
        st.subheader("Aba para Atualizar dados do Usuario")
        todos_usuarios = Usuarios.listar()
        for usuario in todos_usuarios:
            if usurario.get_id
    
        usuario_para_atualizar == Usuarios.listar_id(categoria_id) st.session_state.object_usuario
        if categoria_para_atualizar:
            with st.form("form_atualizar_usuario", clear_on_submit=False):
                nome_atualizado = st.text_input("Nome da Categoria:", value=categoria_para_atualizar.get_nome(), key="nome_usuario_update")
                email_atualizado = st.text_input("Descrição:", value=categoria_para_atualizar.get_descricao(), key="descricao_usuario_update")
                cell_atualizado = st.text_input("Nome da Categoria:", value=categoria_para_atualizar.get_nome(), key="cll_usuario_update")
                senha_atualizado = st.text_input("Nome da Categoria:", value=categoria_para_atualizar.get_nome(), key="senha_usuario_update")
                submit_atualizacao = st.form_submit_button("Atualizar Categoria")

                if submit_atualizacao:
                    if not nome_atualizado or not descricao_atualizada:
                        st.error("Por favor, preencha todos os campos para atualização.")
                    else:
                        try:
                            categoria_atualizada_obj = Categoria(
                                categoria_para_atualizar.get_id(),
                                nome_atualizado,
                                descricao_atualizada
                            )
                            Categorias.atualizar(categoria_atualizada_obj) 
                            st.success(f"Categoria '{nome_atualizado}' atualizada com sucesso!")
                            st.rerun()
                        except ValueError as e:
                            st.error(f"Erro na atualização: {e}")
                        except Exception as e:
                            st.error(f"Ocorreu um erro inesperado: {e}")
        else:
            st.warning("Categoria selecionada não encontrada.")
