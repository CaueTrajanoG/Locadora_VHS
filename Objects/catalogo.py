import os
import sys
import json

#Caminho para o diretório raiz
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root_dir)

#Importando as classes necessárias
from structures.BinarySearchTree import BinarySearchTree
from Objects.filme import Filme
from structures.Exceptions import CatalogoException, AluguelException, DevolucaoException, FilmeException

arv = BinarySearchTree()

with open("Data/filmes.json", encoding="utf-8") as filmes:
    lista_de_filmes = json.load(filmes)

for filme in lista_de_filmes:
    arv.add(Filme(filme['nome'],filme['preco'],filme['disponibilidade']))

def showCat():
    arr = [] 
    arr = arv.returnAll()
    return arr    

def getMovie(title):
    '''
    Função responsável por buscar um filme na árvore e retornar 
    o resultado da busca
    '''
    return arv.search(Filme(title,0,''))

def rentMovie(filme):
    filme.estado = 'Alugado'

def returnMovie(filme):
    filme.estado = 'Disponível'  

def verifyDisp(title):
    filme = getMovie(title)
    if filme:
        if filme.estado == "Disponível":
            rentMovie(filme)
            return "sucesso ao alugar"
        else:
            raise AluguelException("Não foi possivel alugar")
    else:
        raise FilmeException("filme não encontrado")

def verifyRent(title):
    filme = getMovie(title)
    try:
        if filme:
            if filme.estado == "Alugado":
                returnMovie(filme)
                return "filme devolvido com sucesso"
            else:
                raise DevolucaoException("Falha ao devolver o filme")
        else:
            raise DevolucaoException("Filme não encontrado")
    except:
        raise DevolucaoException("Erro no sistema")
        
def get_ticket_str(title):
    '''
    Função responsável por imprimir o ticket de locação do filme
    '''
    movie = getMovie(title)
    titulo = movie.titulo
    preco = str(movie.preco).replace('.', ',')
    
    linha_superior = "       +----------------------------------+"
    linha_inferior = "_ " * (len(linha_superior)//2)
    
    formato_filme = "       |{: ^34}|"
    formato_preco = "       |{: ^34}|"
    formato_mensagem = "       |{: ^33}|"
    
    print(linha_superior)
    print(formato_filme.format("Comprovante"))
    print(formato_filme.format("Filme: {}".format(titulo)))
    print(formato_preco.format("Preço: R${}".format(preco)))
    print(formato_mensagem.format("Bom filme ㋡"))
    print(f'    {linha_inferior}')



