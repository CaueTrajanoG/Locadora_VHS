class Filme:
    def __init__(self, titulo, price, state):
        self.__titulo = titulo
        self.__preco = price
        self.__estado = state

    @property
    def estado(self):
        return self.__estado
    
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def preco(self):
        return self.__preco

    @estado.setter
    def estado(self, novo_estado):
        self.__estado = novo_estado

    def __str__(self):
        return f'{self.__titulo} | {self.__preco} | {self.__estado}'

    def __eq__(self, outro):
        return self.__titulo.lower() == outro.__titulo.lower()

    def __lt__(self, outro):
        return self.__titulo.lower() < outro.__titulo.lower()

    def __gt__(self, outro):
        return self.__titulo.lower() >= outro.__titulo.lower()