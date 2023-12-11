import os
import sys
import json

#Caminho para o diretório raiz
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root_dir)

#Importando as classes necessárias
from structures.BinarySearchTree import BinarySearchTree
from Objects.filme import Filme

arv = BinarySearchTree()

with open("Data/filmes.json", encoding="utf-8") as filmes:
    lista_de_filmes = json.load(filmes)

for filme in lista_de_filmes:
    arv.add(Filme(filme['nome'],filme['preco'],filme['disponibilidade']))

def showCat():
    arr = []
    arr = arv.returnAll()
    #Este for é para testes
    # for i in range(len(arr)):
    #     nome = str(arr[i])
    #     print(nome)
    return arr

def getMovie(title):
    return arv.search(Filme(title,0,''))

def rentMovie(title):
    filme = arv.search(Filme(title,0,''))
    filme.estado = 'Alugado'

def returnMovie(title):
    filme = arv.search(Filme(title,0,''))
    filme.estado = 'disponivel'  

def verifyDisp(title):
    if(arv.search(Filme(title,0,0)) is not None):
        nome = str(arv.search(Filme(title,0,0)))
        nome = nome.split("|")
        if nome[2].strip() == "disponivel":
            rentMovie(nome[0].strip())
            # 902 > sucesso ao alugar
            return "902"
        else:
            # 904 Não foi possivel alugar
            return "904"
    else:
        # 906 filme não encontrado
        return "906"

def verifyRent(title):
    if(arv.search(Filme(title,0,0)) is not None):
        nome = str(arv.search(Filme(title,0,0)))
        nome = nome.split("|")
        if nome[2].strip() == "Alugado":
            returnMovie(nome[0].strip())
            return "Filme devolvido com sucesso."

#Testando o rent e returnMovies
# verifyDisp("casablanca")
# showCat()
# verifyRent("casablanca")
# showCat()



