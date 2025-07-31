import streamlit as st
class Usuario:
    def __init__(self, idPessoa, idProjeto):
        self.set_idPessoa(idPessoa)
        self.set_idProjeto(idProjeto)

    def set_idPessoa(self, idPessoa):
        self.__idPessoa = idPessoa
    def set_idProjeto(self, idProjeto):
        self.__idProjeto = idProjeto

    def get_idPessoa(self): return self.__idPessoa 
    def get_idProjeto(self): return self.__idProjeto
      
    def __str__(self):
        return f"{self.__idPessoa} participa de  {self.__idProjeto}"
    def to_dict(self):
        return {"idPessoal": self.__idPessoa,"idProjeto": self.__idProjeto}
      
    @classmethod
    def from_dict(cls, data):
        return cls(
            idPessoa=data['idPessoa'],
            idProjeto=data['idProjeto']
        )