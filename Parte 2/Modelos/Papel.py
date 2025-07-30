import streamlit as st
class Papel:
    def __inti__(self, id_membro, id_papel):
        self.set_id_membro(id_membro)
        self.set_id_papel(id_papel)

    def set_id_membro(self, id_membro):
        self.__id_membro = id_membro
    def set_id_papel(self, id_papel):
        self.__id_papel = id_papel

    def get_id_membro(self):
        return self.__id_membro
    def get_id_papel(self):
        return self.__id_papel

    def __str__(self):
        return f"{self.__id_membro} - {self.__id_papel}"
    def to_dict(self):
        return {"id": self.__id_membro,"id_papel": self.__id_papel}
      
    @classmethod
    def from_dict(cls, data):
        return cls(
            id_membro=data['id_membro'],
            id_papel=data['id_papel']
        )
