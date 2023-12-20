import os
import sys
import json
from structures.Exceptions import CatalogException

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
    return arr    

def getMovie(title):
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
            # 902 > sucesso ao alugar
            return "902"
        else:
            # 904 > Não foi possivel alugar
            return "904"
    else:
        # 906 > filme não encontrado
        return "906"

def verifyRent(title):
    filme = getMovie(title)
    if filme:
        try:
            if filme.estado == "Alugado":
                returnMovie(filme)
                # 908 > filme devolvido com sucesso 
                return "908"
            else:
                # 912 > filme não está alugado
                return "912"
        except:
            # 910 > falha ao devolver o filme
            return "910"
    # 911 > filme não encontrado
    return "911"
        
def get_ticket_str(title):
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



