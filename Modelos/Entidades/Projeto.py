import streamlit as st
from datetime import datetime
class Projeto:
    def __inti__(self, id, idCriador, nome, descricao, data_comeco, data_fim):
        self.set_id(id)
        self.set_idCriador(idCriador)
        self.set_nome(nome)
        self.set_descricao(descricao)
        self.set_data_comeco(data_comeco)
        self.set_data_fim(data_fim)

    def set_id(self, id):
        self.__id = id
    def set_idCriador(self, idCriador):
        self.__idCriador = idCriador
    def set_nome(self, nome):
        if descricao == "":
            raise ValueError("Informe um nome!)
        self.__nome = nome
    def set_descricao(self, descricao):
        if descricao == "":
            raise ValueError("Informe uma descrição!")
        self.__descricao = descricao
    def set_data_comeco(self, data_comeco):
        if data_comeco == None:
            data_comeco = datetime.now()
        self.__data_comeco = data_comeco
    def set_data_fim(self, data_fim):
        if data_fim == None:
            data_fim = datetime.now()
        self.__data_fim = data_fim

    def get_id(self):
        return self.__id
    def get_idCriador(self):
        return self.idCriador
    def get_nome(self):
        return self.__nome
    def get_descricao(self):
        return self.__descricao
    def get_data_comeco(self):
        return self.__data_comeco
    def get_data_fim(self):
        return self.__data_fim

    def __str__(self):
        return f"{self.__id} - {self.__idCriador} - {self.__nome} - {self.__descricao} - {self.__data_comeco} - {self.__data_fim}"
    def to_dict(self):
        return {"id": self.__id, "idCriador": self.__idCriador, "nome": self.__nome, "descrição": self.__descricao, "começo": self.__data_comeco, "fim": self.__data_fim}
      
    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            idCriador=data['idCriador'],
            nome=data['nome'],
            descricao=data['descriçao'],
            data_comeco=data['começo'],
            data_fim=data['fim']
        )
