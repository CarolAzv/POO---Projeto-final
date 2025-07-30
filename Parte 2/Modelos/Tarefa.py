import streamlit as st
class Tarefa:
    def __init__(self, idProjeto, id, descriçao, status):
        self.set_idProjeto(idProjeto)
        self.set_id(id)
        self.set_descriçao(descriçao)
        self.set_status(status)
      
    def set_idProjeto(self, idProjeto):
        self.__idProjeto = idProjeto
    def set_id(self, id):
        self.__id = id
    def set_descriçao(self, descriçao):
        if descriçao == "": raise ValueError("Descriçao não pode estar vazio")
        self.__descriçao = descriçao
    def set_status(self, status):
        self.__status = status

    def get_idProjeto(self): return self.__idProjeto
    def get_id(self): return self.__id
    def get_descriçao(self): return self.__descriçao
    def get_status(self): return self.__status
      
    def __str__(self):
        return f"{self.__idProjeto} - {self.__id} - {self.__descriçao} - {self.__status}"
    def to_dict(self):
        return {"idProjeto": self.__idProjeto,"id": self.__id,"descrição": self.__descriçao, "status": self.__status}
      
    @classmethod
    def from_dict(cls, data):
        return cls(
            idProjeto=data['idProjeto'],
            id=data['id'],
            descriçao=data['descriçao'],
            status=data['status']
        )
