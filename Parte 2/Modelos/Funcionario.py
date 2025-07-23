import streamlit as st
class Funcionario:
    def __init__(self, id, nome, email, cell, senha):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_cell(cell)
        self.set_senha(senha)
      
    def set_id(self, id):
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Informe seu nome")
        self.__nome = nome
    def set_email(self, email):
        self.__email = email
    def set_cell(self, cell):
        if len(cell) == 11:
            self.__cel = cel
        else: raise ValueError("O número deve está no formato xxxxxxxxxxx - com 11 números")
    def set_senha(self, s):
        if len(s) < 4 : raise ValueError(f"Senha deve ter no mínimo 4 caracteres")
        self.__senha = s

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_cell(self): return self.__cell
    def get_senha(self): return self.__senha
      
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__cell} - {self.__senha}"
    def to_dict(self):
        return {"id": self.__id,"nome": self.__nome,"email": self.__email, "cell": self.__cell, "senha": self.__senha}
      
    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            nome=data['nome'],
            email=data['email'],
            cell=data['cell'],
            senha=data['senha']
        )
