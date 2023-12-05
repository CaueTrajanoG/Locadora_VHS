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
    #--Isto aqui é so para testes!!!
    # for i in range(len(arr)):
    #     nome = str(arr[i])
    #     nome = nome.split("|")
    #     print(nome[0])
    return arr

if(arv.search(Filme("Cidadão Kane",0)) is not None):
    print("Filme Disponivel")
    nome = str(arv.search(Filme("Cidadão Kane",0)))
    nome = nome.split("|")
    print(nome[2])
    if(nome[2]=="disponivel"):
        #funçao que aluga
        pass
    else:
        #return "Não foi possivel"
        pass
else:
    print("Filme indisponivel")


