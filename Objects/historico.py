from structures.Pilha import Pilha
from Objects.catalogo import getMovie


HISTORIES = {}


def create_hist(client):
    HISTORIES[client] = Pilha()
    return HISTORIES[client]

def increment_hist(client, title: str):
    hist = get_hist(client)
    movie = getMovie(title)
    hist.empilha(movie)

def get_all_hist(client):
    hist = get_hist(client)
    return hist.getAll()

def get_hist(client):
    try:
        hist = HISTORIES[client] 
    except KeyError:
        hist = create_hist(client)
    return hist

def print_hist(hist):
    if len(hist) > 0:
        total = 0
        print('\n       ---- Histórico de Aluguéis ----')
        for i in range(len(hist)):
            title = hist[i].titulo
            value = hist[i].preco
            str_value = str(value).replace('.', ',')
            print(f'    -> {i+1:>02} - {title} | Preço: R${str_value}')
            total += hist[i].preco
        str_total = str(round(total, 2)).replace('.', ',')
        print(f'\n    -- Total gasto com aluguéis: R${str_total} --')
    else:
        print('\n---- Histórico vazio. Que tal alugar um filme? ---\n')