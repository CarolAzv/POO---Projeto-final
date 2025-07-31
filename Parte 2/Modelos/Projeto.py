import streamlit as st
from datetime import datetime
class Projeto:
    def __inti__(self, id, descricao, data_comeco, data_fim, status, idPessoa):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_data_comeco(data_comeco)
        self.set_data_fim(data_fim)
        self.set_status(status)
        self.set_idPessoa(idPessoa)

    def set_id(self, id):
        self.__id = id
    def set_descricao(self, descricao):
        if descricao == "":
            raise ValueError("Informe a descrição!")
        self.__descricao = descricao
    def set_data_comeco(self, data_comeco):
        if data_comeco == None:
            data_comeco = datetime.now()
        else:
            self.__data_comeco = data_comeco
        self.__data_comeco = data_comeco
    def set_data_fim(self, data_fim):
        self.__data_fim = data_fim
    def set_status(self, status):
        if status == "":
             raise ValueError("Informe o status!")
        self.__status = status
    def set_idPessoa(self, idPessoa):
        self.__idPessoa = idPessoa

    def get_id(self):
        return self.__id
    def get_descricao(self):
        return self.__descricao
    def get_data_comeco(self):
        return self.__data_comeco
    def get_status(self):
        return self.__status
    def get_idFuncionario(self):
        return self.__idPessoa

    def __str__(self):
        return f"{self.__id} - {self.__descricao} - {self.__data_comeco} - {self.__status} - {self.__idPessoa}"
    def to_dict(self):
        return {"id": self.__id,"descrição": self.__descricao,"Começo": self.__data_comeco, "status": self.__status, "id de membros": self.__idPessoa}
      
    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            descricao=data['descriçao'],
            email=data['data_comeco'],
            cell=data['status'],
            senha=data['idPessoa']
        )
