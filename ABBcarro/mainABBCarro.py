#from ArvoreBinariaBusca import ArvoreBinaria, No
from BinarySearchTree import BinarySearchTree, Node
from Carro import Carro

arv = BinarySearchTree()
arv.add(Carro(123,'Fusca',1970))
arv.add(Carro(456,'Celta', 2002))
arv.add(Carro(777,'Kwid', 2020))
arv.add(Carro(888,'Opala', 1991))
arv.add(Carro(999,'Nissan Kicks', 2023))
arv.add(Carro(174,'Audi Eletrico ultima geracao', 2023))

arv.preorder()
chave = Carro(123, "Fadasddsasca", 220)
print('Busca: ', arv.search(chave))
exit()
