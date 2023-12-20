class CatalogoException(Exception):
  def __init__(self, msg):
    super().__init__(msg)

class AluguelException(Exception):
  def __init__(self, msg):
    super().__init__(msg)
  
class DevolucaoException(Exception):
  def __init__(self,msg):
    super().__init__(msg)

class FilmeException(Exception):
  def __init__(self, msg):
    super().__init__(msg)