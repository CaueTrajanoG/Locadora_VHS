from BinarySearchTree import BinarySearchTree
from Filme import Filme

arv = BinarySearchTree()
arv.add(Filme("Carros 2", 10))
arv.add(Filme("Chaves em acapuco", 99))
arv.add(Filme("V de vendeta", 66))
arv.add(Filme("Transformers 3", 66))
arv.add(Filme("Velozes e Furiosos 3", 66))


def showCat():
    arr = []
    arr = arv.returnAll()
    return arr
    # for i in range(len(arr)):
    #     nome = str(arr[i])
    #     nome = nome.split("|")
    #     print(nome[0])
