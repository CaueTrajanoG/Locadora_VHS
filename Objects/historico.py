from structures.Pilha import Pilha
from Objects.catalogo import getMovie


HISTORIES = {}


def create_hist(client):
    HISTORIES[client] = Pilha()
    return HISTORIES[client]

def increment_hist(cliente, title: str):
    hist = get_hist(cliente)
    movie = getMovie(title)
    hist.empilha(movie.titulo)

def get_all_hist(cliente):
    hist = get_hist(cliente)
    return hist.getAll()

def get_hist(cliente):
    try:
        hist = HISTORIES[cliente] 
    except KeyError:
        hist = create_hist(cliente)
    return hist
        