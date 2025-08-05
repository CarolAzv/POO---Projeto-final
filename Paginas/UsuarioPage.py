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
    if not st.session_state.get('logged_in') or st.session_state.get('tipo_usuario') != 'Usuario':
        st.warning("Acesso negado. Por favor, faça login como administrador.")
        st.session_state.pagina_atual = 'login' 
        st.rerun()
        return
    
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
            with st.form("form_cadastro_cliente", clear_on_submit=True):
                novo_nome = st.text_input("Nome:", key="projeto_nome")
                novo_descricao = st.text_input("Descrição:", key="projeto_descricao")
                submitted_projeto = st.form_submit_button("Criar Projeto")

                if submitted_projeto:
                    if not novo_nome or not novo_descricao:
                        st.error("Por favor, preencha todos os campos.")
                    else:
                        try:
                            novo_projeto = Projeto(id=0, idCriador=AAAAAAA, nome=nome_novo, descricao=novo_descricao, data_comeco=datetime.now(), data_fim = 0)
                            Projetos.inserir(novo_cliente)
                            
                            st.success(f"Cliente '{nome_novo}' cadastrado com sucesso!")
                            
                        except ValueError as e:
                            st.error(f"Erro no cadastro: {e}")
                        except Exception as e:
                            st.error(f"Ocorreu um erro inesperado: {e}")

        elif opcoes_cliente == "Listar Clientes":
            st.subheader("Lista de clientes cadastrados")
            todos_clientes = Clientes.listar()
            if todos_clientes:
                dados_clientes = [c.to_dict() for c in todos_clientes]
                
                df_clientes = pd.DataFrame(dados_clientes) 
                
                st.dataframe(df_clientes) 
            else:
                st.info("Nenhum cliente cadastrado ainda.")
        elif opcoes_cliente == "Listar Compras": 
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
                        st.info("Nenhum item detalhado para este pedido.")
        elif opcoes_cliente == "Atualizar dados do Cliente":
            st.subheader("Atualizar os dados do Cliente")
            todos_clientes = Clientes.listar()
            if not todos_clientes:
                st.info("Nenhum cliente cadastrado para atualizar.")
            else:
                opcoes_clientes_selectbox = [f"{c.get_nome()} (ID: {c.get_id()})" for c in todos_clientes]
                
                cliente_selecionado_str = st.selectbox(
                    "Selecione o cliente para atualizar:",
                    opcoes_clientes_selectbox,
                    key="select_cliente_update"
                )
                
                
                cliente_id_str = cliente_selecionado_str.split('(ID: ')[1][:-1]
                cliente_id = int(cliente_id_str)
                                                                                                                                                                                                                                                                                                                       
                
                cliente_para_atualizar = Clientes.listar_id(cliente_id)

                if cliente_para_atualizar:
                   
                    with st.form("form_atualizar_cliente", clear_on_submit=False):
                        st.write(f"Atualizando cliente ID: {cliente_para_atualizar.get_id()}")
                        nome_atualizado = st.text_input("Nome Completo:", value=cliente_para_atualizar.get_nome(), key="nome_cliente_update")
                        email_atualizado = st.text_input("Email:", value=cliente_para_atualizar.get_email(), key="email_cliente_update")
                        senha_atualizada = st.text_input("Nova Senha (deixe em branco para manter a atual):", type="password", key="senha_cliente_update")
                        fone_atualizado = st.text_input("Telefone:", value=cliente_para_atualizar.get_fone(), key="fone_cliente_update")

                        submit_atualizacao = st.form_submit_button("Atualizar Cliente")

                        if submit_atualizacao:
                            if not nome_atualizado or not email_atualizado or not fone_atualizado:
                                st.error("Por favor, preencha nome, email e telefone.")
                            else:
                                try:
                                    # Cria um novo objeto Cliente com os dados atualizados
                                    # Mantém o ID original
                                    cliente_atualizado_obj = Cliente(
                                        id=cliente_para_atualizar.get_id(),
                                        nome=nome_atualizado,
                                        email=email_atualizado,
                                       
                                        senha=senha_atualizada if senha_atualizada else cliente_para_atualizar.get_senha(),
                                        fone=fone_atualizado
                                    )
                                    
                                    Clientes.atualizar(cliente_atualizado_obj)
                                    st.success(f"Cliente '{nome_atualizado}' atualizado com sucesso!")
                                    st.rerun() 
                                except ValueError as e:
                                    st.error(f"Erro na atualização: {e}")
                                except Exception as e:
                                    st.error(f"Ocorreu um erro inesperado: {e}")
                else:
                    st.warning("Cliente selecionado não encontrado. Por favor, selecione um cliente válido.")
        elif opcoes_cliente == "Excluir Cliente":
            st.subheader("Excluir Cliente")
            todos_clientes = Clientes.listar()
            if not todos_clientes:
                st.info("Nenhum cliente para excluir.")
             else:
                opcoes_clientes_selectbox = [f"{c.get_nome()} (ID: {c.get_id()})" for c in todos_clientes]
                cliente_selecionado_str = st.selectbox(
                    "Selecione o cliente para excluir:",
                    opcoes_clientes_selectbox,
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

    #=======================================================================================================================
    #=======================================================================================================================
    #=======================================================================================================================
    with tab_tarefas:
        st.header("Ver suas Tarefas")
        opcoes_entregadores = st.radio(
            "Selecione uma opção",
            ("Cadastrar Entregador","Listar entregadores","Atualizar dados do Entregador","Excluir Entregador"),
            key = "radio_entregadores"
        )
        if opcoes_entregadores == "Cadastrar Entregador":
            st.subheader("Cadastrar novo Entregador")
            st.write("Preencha os dados para criar a conta.")
            with st.form("form_cadastro_entregador", clear_on_submit=True):
                nome_novo = st.text_input("Nome Completo:", key="cadastro_nome_entregador")
                email_novo = st.text_input("Email:", key="cadastro_email_entregador")
                senha_nova = st.text_input("Senha:", type="password", key="cadastro_senha_entregador")
                fone_novo = st.text_input("Telefone:", key="cadastro_fone_entregador")
                transporte_novo = st.text_input("Transporte de Entregas:",key = "cadastro_transporte")

                submitted_cadastro = st.form_submit_button("Cadastrar Entregador")

                if submitted_cadastro:
                    if not nome_novo or not email_novo or not senha_nova or not fone_novo or not transporte_novo:
                        st.error("Por favor, preencha todos os campos para o cadastro.")
                    else:
                        try:
                            novo_entregador = Entregador(id=0, nome=nome_novo, email=email_novo, senha=senha_nova, fone=fone_novo,transporte=transporte_novo)
                            Entregadores.inserir(novo_entregador)
                            
                            st.success(f"Entregador '{nome_novo}' cadastrado com sucesso!")
                            
                        except ValueError as e:
                            st.error(f"Erro no cadastro: {e}")
                        except Exception as e:
                            st.error(f"Ocorreu um erro inesperado: {e}")
        elif opcoes_entregadores == "Listar entregadores":
            st.subheader("Lista de Entregadores cadastrados")
            todos_entregadores = Entregadores.listar()
            if todos_entregadores:
                dados_entregadores = [c.to_dict() for c in todos_entregadores]
                
                df_entregadores = pd.DataFrame(dados_entregadores) 
                
                st.dataframe(df_entregadores) 
            else:
                st.info("Nenhum entregador cadastrado ainda.")

        elif opcoes_entregadores == "Atualizar dados do Entregador":
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

        elif opcoes_entregadores == "Excluir Entregador":
            st.subheader("Excluir Entregador")
            todos_entregadores = Entregadores.listar()
            if not todos_entregadores:
                st.info("Nenhum entregador para excluir.")
            else:
                opcoes_entregadores_selectbox = [f"{e.get_nome()} (ID: {e.get_id()})" for e in todos_entregadores]
                entregador_selecionado_str = st.selectbox(
                    "Selecione o entregador para excluir:",
                    opcoes_entregadores_selectbox,
                    key="select_entregador_delete"
                )
                entregador_id_str = entregador_selecionado_str.split('(ID: ')[1][:-1]
                entregador_id = int(entregador_id_str)
                entregador_para_excluir = Entregadores.listar_id(entregador_id)

                if entregador_para_excluir:
                    st.warning(f"Tem certeza que deseja excluir o entregador: '{entregador_para_excluir.get_nome()}' (ID: {entregador_para_excluir.get_id()})?")
                    if st.button("Confirmar Exclusão", key="confirm_delete_entregador"):
                        try:
                            Entregadores.excluir(entregador_para_excluir)
                            st.success(f"Entregador '{entregador_para_excluir.get_nome()}' excluído com sucesso!")
                            st.rerun()
                        except ValueError as e:
                            st.error(f"Erro na exclusão: {e}")
                        except Exception as e:
                            st.error(f"Ocorreu um erro inesperado: {e}")
                else:
                    st.warning("Entregador selecionado não encontrado.")

    #=======================================================================================================================
    #=======================================================================================================================
    #=======================================================================================================================
    with tab_atualizarUsuario:
        st.header("Atualizar dados do Usuario")
        opcoes_categorias = st.radio(
            "Selecione uma opção:",
            ("Adicionar Categoria","Listar Categoria","Atualizar Categoria","Excluir Categoria"),
            key = "radio_categorias"
        )
        if opcoes_categorias == "Adicionar Categoria":
            st.subheader("Informe os dados da Categoria")
            with st.form("form_cadastro_categoria", clear_on_submit=True):
                nome = st.text_input("Nome da Categoria:",key = "nome_categoria")
                descricao = st.text_input("Descrição:",key = "descricao_categoria")
                submit_cadastro = st.form_submit_button("Adicionar categoria")
                if submit_cadastro:
                    if not nome or not descricao:
                        st.error("Por favor, preencha os campos para cadastro de categoria")
                    else:
                        try:
                            nova_categoria = Categoria(0,nome,descricao)
                            Categorias.inserir(nova_categoria)
                            st.success(f"Categoria '{nome}' adicionada com sucesso!")
                        except ValueError as e:
                            st.error(f"Erro no cadastro: {e}")
                        except Exception as e:
                            st.error(f"Ocorreu um erro inesperado: {e}")
        elif opcoes_categorias == "Listar Categoria":
            st.subheader(" Aba de Lista de Categorias Cadastradas")
            todas_categorias = Categorias.listar()
            if todas_categorias:
                dados_categorias = [c.to_dict() for c in todas_categorias]
                df_categorias = pd.DataFrame(dados_categorias)
                st.dataframe(df_categorias)
            else:
                st.info("Nenhuma categoria cadastrada ainda.")

        elif opcoes_categorias == "Atualizar Categoria":
            st.subheader("Aba para Atualizar dados da Categoria")
            todas_categorias = Categorias.listar() 
            if not todas_categorias:
                st.info("Nenhuma categoria para atualizar.") 
            else:
                nomes_categorias = [f"{c.get_nome()} (ID: {c.get_id()})" for c in todas_categorias]
                categoria_selecionada_nome = st.selectbox(
                    "Selecione a categoria para atualizar:",
                    nomes_categorias,
                    key="select_categoria_update"
                )
                categoria_id_str = categoria_selecionada_nome.split('(ID: ')[1][:-1]
                categoria_id = int(categoria_id_str)
    
                categoria_para_atualizar = Categorias.listar_id(categoria_id)
                if categoria_para_atualizar:
                    with st.form("form_atualizar_categoria", clear_on_submit=False):
                        nome_atualizado = st.text_input("Nome da Categoria:", value=categoria_para_atualizar.get_nome(), key="nome_categoria_update")
                        descricao_atualizada = st.text_input("Descrição:", value=categoria_para_atualizar.get_descricao(), key="descricao_categoria_update")
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
        elif opcoes_categorias == "Excluir Categoria":
            st.subheader("Aba pra Excluir uma Categoria")
            todas_categorias = Categorias.listar()
            if not todas_categorias:
                st.info("Nenhuma categoria para excluir.")
            else:
                nomes_categorias = [f"{c.get_nome()} (ID: {c.get_id()})" for c in todas_categorias]
                categoria_selecionada_nome = st.selectbox(
                    "Selecione a categoria para excluir:",
                    nomes_categorias,
                    key="select_categoria_delete"
                )

               
                categoria_id_str = categoria_selecionada_nome.split('(ID: ')[1][:-1]
                categoria_id = int(categoria_id_str)
                categoria_para_excluir = Categorias.listar_id(categoria_id)

                if categoria_para_excluir:
                    st.warning(f"Tem certeza que deseja excluir a categoria: '{categoria_para_excluir.get_nome()}' (ID: {categoria_para_excluir.get_id()})?")
                    if st.button("Confirmar Exclusão", key="confirm_delete_categoria"):
                        try:
                            Categorias.excluir(categoria_para_excluir.get_id())
                            st.success(f"Categoria '{categoria_para_excluir.get_nome()}' excluída com sucesso!")
                            st.rerun() 
                        except ValueError as e:
                            st.error(f"Erro na exclusão: {e}")
                        except Exception as e:
                            st.error(f"Ocorreu um erro inesperado: {e}")
                else:
                    st.warning("Categoria selecionada não encontrada.")
    with tab_produtos:
        st.header("Gerenciar Produtos")
        opcoes_produtos = st.radio(
            "Selecione uma opção:",
            ("Adicionar Produto","Listar Produtos","Atualizar Produto","Reajustar preço de Produto","Excluir Produto"),
            key = "radio_produtos"
        )
        if opcoes_produtos == "Adicionar Produto":
            st.subheader("Cadastrar Novo Produto")
            todas_categorias = Categorias.listar()
            if not todas_categorias:
                st.warning("Nenhuma categoria cadastrada. Cadastre uma categoria antes de adicionar produtos.")
            else:
                opcoes_selectbox_categorias = {f"{c.get_nome()} (ID: {c.get_id()})": c for c in todas_categorias}
                nomes_categorias_para_selectbox = list(opcoes_selectbox_categorias.keys())

                categoria_selecionada_nome = st.selectbox(
                    "Selecione a Categoria do Produto:",
                    nomes_categorias_para_selectbox,
                    key="select_categoria_produto_add"
                )
                categoria_id_str = categoria_selecionada_nome.split('(ID: ')[1][:-1]
                categoria_id = int(categoria_id_str)

                with st.form("form_cadastro_produto", clear_on_submit=True):
                    nome_produto = st.text_input("Nome do Produto:", key="nome_produto_add")
                    descricao_produto = st.text_input("Descrição:", key="descricao_produto_add")
                    preco_produto = st.number_input("Preço (R$):", min_value=0.01, format="%.2f", key="preco_produto_add")
                     estoque_produto = st.number_input("Estoque:", min_value=0, step=1, key="estoque_produto_add")

                    submit_cadastro_produto = st.form_submit_button("Adicionar Produto")

                    if submit_cadastro_produto:
                        if not nome_produto or not descricao_produto or preco_produto <= 0 or estoque_produto < 0:
                            st.error("Por favor, preencha todos os campos e garanta valores válidos.")
                        else:
                            try:
                                novo_produto = Produto(
                                    id=0,
                                    nome=nome_produto,
                                    descricao=descricao_produto,
                                    preco=preco_produto,
                                    estoque=estoque_produto,
                                    categoria_id=categoria_id 
                                )
                                Produtos.inserir(novo_produto)
                                categoria_obj_para_msg = Categorias.listar_id(categoria_id)
                                categoria_nome_para_msg = categoria_obj_para_msg.get_nome() if categoria_obj_para_msg else "Desconhecida"
                                st.success(f"Produto '{nome_produto}' adicionado com sucesso na categoria '{categoria_nome_para_msg}'!")
                            except ValueError as e:
                                st.error(f"Erro no cadastro do produto: {e}")
                            except Exception as e:
                                st.error(f"Ocorreu um erro inesperado: {e}")

        
        elif opcoes_produtos == "Listar Produtos":
            st.subheader("Lista de Produtos Cadastrados")
            todos_produtos = Produtos.listar()
            if todos_produtos:
                dados_produtos = []
                for p in todos_produtos:
                    p_dict = p.to_dict()
            
                    categoria = Categorias.listar_id(p.get_id_categoria())
                    p_dict['categoria_nome'] = categoria.get_nome() if categoria else "Desconhecida"
                    dados_produtos.append(p_dict)

                df_produtos = pd.DataFrame(dados_produtos)

                column_config = {
                    "preco": st.column_config.NumberColumn(
                        "Preço (R$)",
                        format="%.2f",
                        help="Preço do produto em Reais"
                    )
                }

                colunas_ordenadas = ['id', 'nome', 'categoria_nome', 'descricao', 'preco', 'estoque']
                df_produtos = df_produtos[colunas_ordenadas]
                st.dataframe(df_produtos, column_config=column_config, use_container_width=True)
            else:
                st.info("Nenhum produto cadastrado ainda.")

        elif opcoes_produtos == "Atualizar Produto":
            st.subheader("Atualizar Dados do Produto")
            todos_produtos = Produtos.listar()
            if not todos_produtos:
                st.info("Nenhum produto para atualizar.")
            else:
                nomes_produtos = [f"{p.get_nome()} (ID: {p.get_id()})" for p in todos_produtos]
                produto_selecionado_nome = st.selectbox(
                    "Selecione o produto para atualizar:",
                    nomes_produtos,
                    key="select_produto_update"
                )
                produto_id_str = produto_selecionado_nome.split('(ID: ')[1][:-1]
                produto_id = int(produto_id_str)
                produto_para_atualizar = Produtos.listar_id(produto_id)

                if produto_para_atualizar:
                    todas_categorias = Categorias.listar()
                    opcoes_selectbox_categorias = {f"{c.get_nome()} (ID: {c.get_id()})": c for c in todas_categorias}
                    nomes_categorias_para_selectbox = list(opcoes_selectbox_categorias.keys())

                    categoria_atual_index = 0
                    if produto_para_atualizar.get_id_categoria():
                        for i, c in enumerate(todas_categorias):
                            if c.get_id() == produto_para_atualizar.get_id_categoria():
                                categoria_atual_index = i
                                break

                    with st.form("form_atualizar_produto", clear_on_submit=False):
                        st.write(f"Atualizando produto ID: {produto_para_atualizar.get_id()}")

                        categoria_selecionada_update_nome = st.selectbox(
                            "Selecione a Nova Categoria do Produto:",
                            nomes_categorias_para_selectbox,
                            index=categoria_atual_index, 
                            key="select_categoria_produto_update"
                        )
                        categoria_id_update_str = categoria_selecionada_update_nome.split('(ID: ')[1][:-1]
                        categoria_id_update = int(categoria_id_update_str)

                        nome_atualizado = st.text_input("Nome do Produto:", value=produto_para_atualizar.get_nome(), key="nome_produto_update")
                        descricao_atualizada = st.text_input("Descrição:", value=produto_para_atualizar.get_descricao(), key="descricao_produto_update")
                        estoque_atualizado = st.number_input("Estoque:", value=produto_para_atualizar.get_estoque(), min_value=0, step=1, key="estoque_produto_update")

                        submit_atualizacao_produto = st.form_submit_button("Atualizar Produto")

                        if submit_atualizacao_produto:
                            if not nome_atualizado or not descricao_atualizada or  estoque_atualizado < 0:
                                st.error("Por favor, preencha todos os campos e garanta valores válidos.")
                            else:
                                try:
                                    produto_atualizado_obj = Produto(
                                        id=produto_para_atualizar.get_id(),
                                        nome=nome_atualizado,
                                        descricao=descricao_atualizada,
                                        preco=produto_para_atualizar.get_preco(),
                                        estoque=estoque_atualizado,
                                        categoria_id=categoria_id_update 
                                     )
                                    Produtos.atualizar(produto_atualizado_obj)
                                    st.success(f"Produto '{nome_atualizado}' atualizado com sucesso!")
                                    st.rerun()
                                except ValueError as e:
                                    st.error(f"Erro na atualização do produto: {e}")
                                except Exception as e:
                                    st.error(f"Ocorreu um erro inesperado: {e}")
                else:
                    st.warning("Produto selecionado não encontrado.")

        elif opcoes_produtos == "Reajustar preço de Produto":
            st.subheader("Reajustar Preço de Produto")
            todos_produtos = Produtos.listar()
            if not todos_produtos:
                st.info("Nenhum produto cadastrado para reajustar o preço.")
            else:
                nomes_produtos = [f"{p.get_nome()} (ID: {p.get_id()})" for p in todos_produtos]
                produto_selecionado_reajuste_nome = st.selectbox(
                    "Selecione o produto para reajustar o preço:",
                    nomes_produtos,
                    key="select_produto_reajuste"
                )
                produto_id_reajuste_str = produto_selecionado_reajuste_nome.split('(ID: ')[1][:-1]
                produto_id_reajuste = int(produto_id_reajuste_str)
                produto_para_reajustar = Produtos.listar_id(produto_id_reajuste)

                if produto_para_reajustar:
                    st.write(f"Preço atual de '{produto_para_reajustar.get_nome()}': R${produto_para_reajustar.get_preco():.2f}")
                    percentual_reajuste = st.number_input(
                        "Percentual de Reajuste (ex: 10 para 10% de aumento, -5 para 5% de desconto):",
                        min_value=-100.0, max_value=100.0, value=0.0, format="%.2f", key="percentual_reajuste"
                    )
                    if st.button("Aplicar Reajuste", key="apply_reajuste_produto"):
                        try:
                            novo_preco = produto_para_reajustar.get_preco() * (1 + percentual_reajuste / 100)
                            
                            # Cria um novo objeto Produto com o preço reajustado
                            produto_reajustado_obj = Produto(
                                id=produto_para_reajustar.get_id(),
                                nome=produto_para_reajustar.get_nome(),
                                descricao=produto_para_reajustar.get_descricao(),
                                preco=novo_preco, # Preço atualizado
                                estoque=produto_para_reajustar.get_estoque(),
                                categoria_id=produto_para_reajustar.get_id_categoria()
                            )
                            Produtos.atualizar(produto_reajustado_obj)
                            st.success(f"Preço de '{produto_reajustado_obj.get_nome()}' reajustado para R${novo_preco:.2f} com sucesso!")
                            st.rerun()
                        except ValueError as e:
                            st.error(f"Erro ao reajustar preço: {e}")
                        except Exception as e:
                            st.error(f"Ocorreu um erro inesperado ao reajustar o preço: {e}")
                else:
                    st.warning("Produto selecionado não encontrado.")


        elif opcoes_produtos == "Excluir Produto":
            st.subheader("Excluir Produto")
            todos_produtos = Produtos.listar()
            if not todos_produtos:
                st.info("Nenhum produto para excluir.")
            else:
                nomes_produtos = [f"{p.get_nome()} (ID: {p.get_id()})" for p in todos_produtos]
                produto_selecionado_nome = st.selectbox(
                    "Selecione o produto para excluir:",
                    nomes_produtos,
                    key="select_produto_delete"
                )
                produto_id_str = produto_selecionado_nome.split('(ID: ')[1][:-1]
                produto_id = int(produto_id_str)
                produto_para_excluir = Produtos.listar_id(produto_id)

                if produto_para_excluir:
                    st.warning(f"Tem certeza que deseja excluir o produto: '{produto_para_excluir.get_nome()}' (ID: {produto_para_excluir.get_id()})?")
                    if st.button("Confirmar Exclusão", key="confirm_delete_produto"):
                        try:
                            Produtos.excluir(produto_para_excluir) # Passa o objeto completo
                            st.success(f"Produto '{produto_para_excluir.get_nome()}' excluído com sucesso!")
                            st.rerun()
                        except ValueError as e:
                            st.error(f"Erro na exclusão do produto: {e}")
                        except Exception as e:
                            st.error(f"Ocorreu um erro inesperada: {e}")
                else:
                    st.warning("Produto selecionado não encontrado.")

    with tab_entregas:
        st.header("Gerenciar Entregas")
        opcoes_entregas = st.radio(
            "Selecione uma opção:",
            ("Atribuir Entrega", "Listar Entregas", "Atualizar Status de Entrega"),
            key="radio_entregas_admin"
        )

        if opcoes_entregas == "Atribuir Entrega":
            st.subheader("Atribuir Entregador a um Pedido")

            pedidos_para_atribuicao = Pedidos.listar_pedidos_para_atribuicao()

            if not pedidos_para_atribuicao:
                st.info("Nenhum pedido pendente de atribuição no momento.")
            else:
                opcoes_pedidos_selectbox = []
                pedidos_map = {}
                for p in pedidos_para_atribuicao:
                    cliente = Clientes.listar_id(p.get_cliente_id())
                    cliente_nome = cliente.get_nome() if cliente else "Cliente Desconhecido"
                    opcao_str = f"Pedido ID: {p.get_id()} - Cliente: {cliente_nome} - Valor: R${p.get_valor_total():.2f} - Status: {p.get_status()}"
                    opcoes_pedidos_selectbox.append(opcao_str)
                    pedidos_map[opcao_str] = p

                pedido_selecionado_str = st.selectbox(
                    "Selecione o Pedido para Atribuir:",
                    opcoes_pedidos_selectbox,
                    key=f"select_pedido_atribuir_{opcoes_entregas}"
                )

                pedido_para_atribuir = pedidos_map.get(pedido_selecionado_str)

                if pedido_para_atribuir:
                    st.write(f"**Detalhes do Pedido Selecionado:**")
                    st.write(f"ID do Pedido: {pedido_para_atribuir.get_id()}")
                    cliente_do_pedido = Clientes.listar_id(pedido_para_atribuir.get_cliente_id())
                    if cliente_do_pedido:
                        st.write(f"Cliente: {cliente_do_pedido.get_nome()}")
                        st.write(f"Endereço de Entrega: {pedido_para_atribuir.get_endereco()}")
                    else:
                        st.write("Cliente: Desconhecido")
                    st.write(f"Valor Total: R${pedido_para_atribuir.get_valor_total():.2f}")
                    st.write(f"Status Atual: {pedido_para_atribuir.get_status()}")
                    
                    if pedido_para_atribuir.get_itens_pedidos(): 
                        st.write("**Itens:**")
                        for item in pedido_para_atribuir.get_itens_pedidos(): 
                            produto = Produtos.listar_id(item.get('produto_id'))
                            produto_nome = produto.get_nome() if produto else "Produto Desconhecido"
                            st.write(f"- {produto_nome} (Qtd: {item.get('quantidade')}, R${item.get('preco_unitario'):.2f} cada)")
                    else:
                        st.info("Nenhum item detalhado para este pedido.")


                    st.markdown("---")

                    todos_entregadores = Entregadores.listar()
                    
                    if not todos_entregadores:
                        st.warning("Nenhum entregador cadastrado. Cadastre entregadores antes de atribuir entregas.")
                    else:
                        opcoes_entregadores_selectbox = [f"{e.get_nome()} (ID: {e.get_id()})" for e in todos_entregadores]
                        entregador_selecionado_str = st.selectbox(
                            "Selecione o Entregador para este Pedido:",
                            opcoes_entregadores_selectbox,
                            key=f"select_entregador_atribuir_{opcoes_entregas}"
                        )
                        entregador_id_str = entregador_selecionado_str.split('(ID: ')[1][:-1]
                        entregador_id_selecionado = int(entregador_id_str)
                        entregador_atribuido_obj = Entregadores.listar_id(entregador_id_selecionado)

                        if st.button("Confirmar Atribuição de Entrega", key=f"confirm_assign_delivery_{opcoes_entregas}"):
                            try:
                                pedido_para_atribuir.set_entregador_id(entregador_id_selecionado)
                                pedido_para_atribuir.set_status("Em Rota de Entrega")
                                
                                Pedidos.atualizar(pedido_para_atribuir)
                                st.success(f"Pedido ID {pedido_para_atribuir.get_id()} atribuído a '{entregador_atribuido_obj.get_nome()}' com sucesso! Status: 'Em Rota de Entrega'.")
                                st.rerun()
                            except ValueError as e:
                                st.error(f"Erro ao atribuir entrega: {e}")
                            except Exception as e:
                                st.error(f"Ocorreu um erro inesperado ao atribuir a entrega: {e}")
                else:
                    st.warning("Pedido selecionado não encontrado. Por favor, selecione um pedido válido.")

        elif opcoes_entregas == "Listar Entregas":
            st.subheader("Lista de Todas as Entregas (Pedidos)")
            todos_pedidos = Pedidos.listar()
            if todos_pedidos:
                dados_pedidos = []
                for p in todos_pedidos:
                    p_dict = p.to_dict()
                    cliente = Clientes.listar_id(p.get_cliente_id())
                    p_dict['cliente_nome'] = cliente.get_nome() if cliente else "Desconhecido"
                    
                    entregador = Entregadores.listar_id(p.get_entregador_id()) if p.get_entregador_id() else None
                    p_dict['entregador_nome'] = entregador.get_nome() if entregador else "Não Atribuído"
                    
                    p_dict['data_pedido'] = p.get_data_pedido().strftime("%d/%m/%Y %H:%M")
                    p_dict['data_entrega'] = p.get_data_entrega().strftime("%d/%m/%Y %H:%M") if p.get_data_entrega() else "N/A"

                    dados_pedidos.append(p_dict)

                df_pedidos = pd.DataFrame(dados_pedidos)
                
                column_config_pedidos = {
                    "valor_total": st.column_config.NumberColumn(
                        "Valor Total (R$)",
                        format="%.2f",
                        help="Valor total do pedido"
                    )
                }

                colunas_ordenadas_pedidos = [
                    'id', 'cliente_nome', 'entregador_nome', 'status', 'valor_total',
                    'endereco_entrega', 'data_pedido', 'data_entrega'
                ]
                df_pedidos = df_pedidos[colunas_ordenadas_pedidos]
                st.dataframe(df_pedidos, column_config=column_config_pedidos, use_container_width=True)
            else:
                st.info("Nenhum pedido cadastrado ainda.")

        elif opcoes_entregas == "Atualizar Status de Entrega":
            st.subheader("Atualizar Status de Entrega de um Pedido")
            todos_pedidos = Pedidos.listar()
            if not todos_pedidos:
                st.info("Nenhum pedido para atualizar o status.")
            else:
                opcoes_pedidos_status_selectbox = []
                pedidos_status_map = {}
                for p in todos_pedidos:
                    cliente = Clientes.listar_id(p.get_cliente_id())
                    cliente_nome = cliente.get_nome() if cliente else "Cliente Desconhecido"
                    entregador = Entregadores.listar_id(p.get_entregador_id()) if p.get_entregador_id() else None
                    entregador_nome = entregador.get_nome() if entregador else "Não Atribuído"
                    opcao_str = f"Pedido ID: {p.get_id()} - Cliente: {cliente_nome} - Entregador: {entregador_nome} - Status Atual: {p.get_status()}"
                    opcoes_pedidos_status_selectbox.append(opcao_str)
                    pedidos_status_map[opcao_str] = p

                pedido_selecionado_status_str = st.selectbox(
                    "Selecione o Pedido para Atualizar o Status:",
                    opcoes_pedidos_status_selectbox,
                    key=f"select_pedido_status_update_{opcoes_entregas}"
                )
                pedido_para_atualizar_status = pedidos_status_map.get(pedido_selecionado_status_str)

                if pedido_para_atualizar_status:
                    st.write(f"**Pedido ID:** {pedido_para_atualizar_status.get_id()}")
                    st.write(f"**Status Atual:** {pedido_para_atualizar_status.get_status()}")

                    novos_status_possiveis = [
                        "Pendente", "Em Preparacao", "Pronto para Entrega",
                        "Em Rota de Entrega", "Entregue", "Cancelado"
                    ]
                    current_status_index = novos_status_possiveis.index(pedido_para_atualizar_status.get_status()) if pedido_para_atualizar_status.get_status() in novos_status_possiveis else 0

                    novo_status = st.selectbox(
                        "Selecione o Novo Status:",
                        novos_status_possiveis,
                        index=current_status_index,
                        key=f"select_new_status_pedido_{opcoes_entregas}"
                    )

                    if st.button("Atualizar Status do Pedido", key=f"update_pedido_status_button_{opcoes_entregas}"):
                        try:
                            pedido_para_atualizar_status.set_status(novo_status)
                            if novo_status == "Entregue":
                                pedido_para_atualizar_status.set_data_entrega(datetime.now())
                            elif pedido_para_atualizar_status.get_data_entrega() is not None and novo_status != "Entregue":
                                pedido_para_atualizar_status.set_data_entrega(None)

                            Pedidos.atualizar(pedido_para_atualizar_status)
                            st.success(f"Status do Pedido ID {pedido_para_atualizar_status.get_id()} atualizado para '{novo_status}' com sucesso!")
                            st.rerun()
                        except ValueError as e:
                            st.error(f"Erro ao atualizar status: {e}")
                        except Exception as e:
                            st.error(f"Ocorreu um erro inesperado ao atualizar o status: {e}")
                else:
                    st.warning("Pedido selecionado não encontrado.")
