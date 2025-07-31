import json
import os 
from Modelos.Entidades.Papel import Papel
import streamlit as st
class Papeis:
    objetos = [] 
    FILE_PATH = 'Data/papel.json'

    @classmethod 
    def inserir(cls, obj):
        cls.abrir() 
        m = max((x.get_id() for x in cls.objetos), default=0)
        obj.set_id(m + 1)
        cls.objetos.append(obj)
        cls.salvar() 

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.get_id() == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        found = False
        for i, item in enumerate(cls.objetos):
            if item.get_id() == obj.get_id():
                cls.objetos[i] = obj 
                found = True
                break
        if found:
            cls.salvar()
        else:
            raise ValueError(f"Usuario com ID {obj.get_id()} não encontrado para atualização.")

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        original_len = len(cls.objetos)
        cls.objetos = [item for item in cls.objetos if item.get_id() != obj.get_id()]
        if len(cls.objetos) < original_len:
            cls.salvar()
        else:
            raise ValueError(f"Usuario com ID {obj.get_id()} não encontrado para exclusão.")

    @classmethod
    def listar_nome(cls, nome):
        cls.abrir()
        for obj in cls.objetos:
            if obj.get_nome() == nome:
                return obj
        return None

    @classmethod
    def listar_email(cls, email: str):
        cls.abrir()
        for obj in cls.objetos:
            if obj.get_email().lower() == email.lower(): # Compara em minúsculas
                return obj
        return None

    @classmethod
    def abrir(cls):
        cls.objetos = [] 
        os.makedirs(os.path.dirname(cls.FILE_PATH), exist_ok=True)
        try:
            if os.path.exists(cls.FILE_PATH) and os.path.getsize(cls.FILE_PATH) > 0:
                with open(cls.FILE_PATH, "r", encoding='utf-8') as arquivo:
                    dados = json.load(arquivo)
                    for d in dados:
                        obj = Usuario.from_dict(d)
                        cls.objetos.append(obj)
            else:
                with open(cls.FILE_PATH, 'w', encoding='utf-8') as f:
                    json.dump([], f, indent=4)
        except json.JSONDecodeError:
            cls.objetos = []
            st.write(f"Atenção: O arquivo '{cls.FILE_PATH}' está corrompido ou vazio. Inicializando com dados vazios.")
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open(cls.FILE_PATH, "w", encoding='utf-8') as arquivo:
            json.dump([obj.to_dict() for obj in cls.objetos], arquivo, indent=4, ensure_ascii=False)