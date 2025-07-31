import streamlit as st
class Usuario:
    def __init__(self, id, idUsuario, idProjeto):
        self.set_id(id)
        self.set_idUsuario(idUsuario)
        self.set_idProjeto(idProjeto)

    def set_id(self, id):
        self.__id = id
    def set_idUsuario(self, idUsuario):
        self.__idUsuario = idUsuario
    def set_idProjeto(self, idProjeto):
        self.__idProjeto = idProjeto

    def get_id(self): return self.__id
    def get_idUsuario(self): return self.id__Usuario 
    def get_idProjeto(self): return self.__idProjeto
      
    def __str__(self):
        return f"{self.__id} - {self.__idUsuario} participa de  {self.__idProjeto}"
    def to_dict(self):
        return {"id": self.__id, "Usuario": self.__idUsuario, "Projeto": self.__idProjeto}
      
    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            idUsuario=data['Usuario'],
            idProjeto=data['Projeto']
        )