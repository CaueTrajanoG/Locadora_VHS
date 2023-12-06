import pickle
import socket

HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor está

# abre um socket UDP
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
msg = ""
pagina = 1


def ticket(title):
    print('+---------------------------------+')
    print('|         Comprovante             |')
    print(f'| Filme: {title:<26}|')
    print(f'| Preço: 18,90 R$                |')
    print('|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _| ')

def showMenu():
    print('''
Opções:
          +___________________+
          ||                 ||
    ►     || Catálogo        ||
    ►     || Alugar          ||
    ►     || Devolver        ||
    ►     || Sair            ||
          ||_________________|| 
''')

while True:    
    if pagina == 1:
        showMenu()
    print(" ►", end=" ")
    msg = input()

    try:
        if msg == "catalogo":
            pagina = 2
            tcp.send(msg.encode())
            data_serialized = tcp.recv(4096)           
            data_received = pickle.loads(data_serialized)
            print()
            print("     ========================== Filmes ===========================")
            for i in range(len(data_received)):
                nome = str(data_received[i])
                nome = nome.split("|")
                print(f'  ►  {nome[0]:<60} :: {nome[2]}')
            print()
            print("         -=-=-=-=-=-=-=-= MENU -=-=-=-=-=-=-=-")
            print("         | alugar | devolver | voltar | sair |")
            print("         =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        elif msg =="alugar":
            tcp.send(msg.encode())
            fita = input("Fita: ")
            msg = fita
            tcp.send(msg.encode())
            retorno = tcp.recv(1024)
            retorno = retorno.decode()
            ticket(fita)
            print(retorno)

            pagina = 1
        elif msg =="devolver":
            tcp.send(msg.encode())
            fita = input("Fita: ")
            msg = fita
            tcp.send(msg.encode())
            retorno = tcp.recv(1024)
            retorno = retorno.decode()
            print(retorno)
            pagina = 1
        else:
            pagina = 1

    except Exception as e:
        print('Erro:', e)
        print("Conexão encerrada")
    if msg == "s" or msg == "sair":
        break
tcp.close()
