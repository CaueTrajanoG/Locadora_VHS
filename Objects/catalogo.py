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
    for i in range(len(arr)):
                nome = str(arr[i])
                print(nome)
                # print(f'    {i+1:<5} ►  {nome[0]:<60} :: {nome[2]}')
    # return arr

def rentMovie(title):
    filme = arv.deleteNode(Filme(title,0,''))
    if filme.estado == 'disponivel':
        filme.estado = 'indisponivel'
        print('Filme alugado')
    else:
        print('Este filme está disponivel')


def verifyDisp(title):
    if(arv.search(Filme(title,0,0)) is not None):
        print("Filme existe")
        nome = str(arv.search(Filme(title,0,0)))
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
verifyDisp("Casablanca")


