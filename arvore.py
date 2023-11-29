class ArvoreException(Exception):
    def __init__(self,mensagem):
        super().__init__(mensagem)


class No:
    def __init__(self, filme):
        self.filme = filme
        self.__esq = None
        self.__dir = None
    
  
def preorder(node):
    if node is not None:
        print(node.carga, end=' ')
        preorder(node.esq)
        preorder(node.dir)


