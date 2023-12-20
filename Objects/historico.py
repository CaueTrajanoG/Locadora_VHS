from structures.Pilha import Pilha
from Objects.catalogo import getMovie


# Dicionário contendo todos os históricos dos usuários
# O dicionário é inicializado vazio
HISTORIES = {}


def create_hist(client):
    '''
    Função responsável por criar o histórico do usuário e retorná-lo
    '''
    HISTORIES[client] = Pilha()
    return HISTORIES[client]

def increment_hist(client, title: str):
    '''
    Função responsável por incrementar o histórico de locações do usuário
    '''
    hist = get_hist(client)
    movie = getMovie(title)
    hist.empilha(movie)

def get_all_hist(client):
    '''
    Função responsável por buscar e devolver o histórico de locações do usuário
    '''
    hist = get_hist(client)
    return hist.getAll()

def get_hist(client):
    '''
    Função responsável por buscar ou criar, caso não exista, o histórico
    de locações do usuário
    '''
    try:
        hist = HISTORIES[client] 
    except KeyError:
        hist = create_hist(client)
    return hist

def print_hist(hist):
    '''
    Função responsável por imprimir o histórico de aluguéis do usuário
    '''
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