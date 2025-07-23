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
    self.__descricao = descricao
  def set_data_comeco(self, data_comeco):
    self.__data_comeco = data_comeco
  def set_status(self, status):
    self.__status = status
  def set_idFuncionario(self, idFuncionario):
    self.__idFuncionario = idFuncionario
