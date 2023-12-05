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
    arv.add(Filme(filme['nome'],filme['preco']))

def showCat():
    arr = []
    arr = arv.returnAll()
    return arr

def rentMovie(title):
    filme = str(arv.deleteNode(Filme(title,0)))
    filme = filme.split("|")    
    arv.add(filme[0].strip(), filme[1].strip())

def verifyDisp(title):
    if(arv.search(Filme(title,0)) is not None):
        print("Filme existe")
        nome = str(arv.search(Filme(title,0)))
        nome = nome.split("|")
        print(nome[2].strip())
        rentMovie(nome[0].strip())
        if(nome[2]=="disponivel"):
            #funçao que aluga
            pass
        else:
            #return "Não foi possivel"
            pass
    else:
        print("Filme indisponivel")
verifyDisp("Casablanca")


