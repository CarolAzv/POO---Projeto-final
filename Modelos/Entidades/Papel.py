import streamlit as st
class Papel:
    def __inti__(self, idMembro, papel):
        self.set_idMembro(idMembro)
        self.set_papel(papel)

    def set_idMembro(self, idMembro):
        self.__idMembro = idMembro
    def set_papel(self, papel):
        if nome == "": raise ValueError("Informe seu papel!")
        self.__papel = papel

    def get_idMembro(self):
        return self.__idMembro
    def get_papel(self):
        return self.__papel

    def __str__(self):
        return f"{self.__idMembro} - {self.__papel}"
    def to_dict(self):
        return {"idMembro": self.__idMembro,"papel": self.__papel}
      
    @classmethod
    def from_dict(cls, data):
        return cls(
            idMembro=data['idMembro'],
            papel=data['papel']
        )
