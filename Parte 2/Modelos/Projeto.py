from datetime import datetime
class Projetos:
  def __inti__(self, id, descricao, data_comeco, status, idFuncionario):
    self.set_id(id)
    self.set_descricao(descricao)
    self.set_data_comeco(data_comeco)
    self.set_status(status)
    self.set_idFuncionario(idFuncionario)

  def set_id(self, id):
    self.__id = id
  def set_descricao(self, descricao):
    if descricao == "":
            raise ValueError("Informe a descrição!")
    self.__descricao = descricao
  def set_data_comeco(self, data_comeco):
     if d == "":
            raise ValueError("A data de começo não pode está vazia!")
    self.__data_comeco = data_comeco
  def set_status(self, status):
    if status == "":
             raise ValueError("Informe o status!")
    self.__status = status
  def set_idFuncionario(self, idFuncionario):
    self.__idFuncionario = idFuncionario

  def get_id(self):
    return self.__id
  def get_descricao(self):
    return self.__descricao
  def get_data_comeco(self):
    return self.__data_comeco
  def get_status(self):
    return self.__status
  def get_idFuncionario(self):
    return self.__idFuncionario
