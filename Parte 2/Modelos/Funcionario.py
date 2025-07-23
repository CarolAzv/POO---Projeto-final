import streamlit as st
class Cliente:
    def __init__(self, id, nome, email, fone, senha):
        self.__id = id
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_senha(senha)
      
    def set_id(self, id):
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Informe seu nome")
        self.__nome = nome
    def set_email(self, email):
        self.__email = email
    def set_fone(self, fone):
        if len(fone) == 11:
            self.__fone = fone
        else: raise ValueError("O número deve está no formato xxxxxxxxxxx - com 11 números")
    def set_senha(self,s):
        if len(s) < 4 : raise ValueError(f"Senha deve ter no mínimo 4 caracteres")
        self.__senha = s

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
    def get_senha(self): return self.__senha
      
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__senha} - {self.__fone} - {self.__endereco}"
    def to_dict(self):
        return {"id": self.__id,"nome": self.__nome,"email": self.__email, "senha": self.__senha, "fone": self.__fone,"endereco":self.__endereco}
      
    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            nome=data['nome'],
            email=data['email'],
            fone=data['fone'],
            senha=data['senha']
        )
