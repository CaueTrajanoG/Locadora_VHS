import pickle
import socket
import time
from env import HOST, PORT

# abre um socket UDP
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
msg = ""
pagina = 1

connected = False
while not connected:
    try:
        tcp.connect(dest)
        connected = True
    except ConnectionRefusedError:
        print(
            f'Não foi possível se conectar com o HOST {HOST} na PORTA {PORT}\n'
            f'Tentando novamente...')
        time.sleep(30)

def ticket(title):
    print(f'+---------------------------------+')
    print(f'|         Comprovante             |')
    print(f'| Filme: {title:<26}|'              )
    print(f'| Preço: 18,90 R$                 |')
    print(f'| Bom filme ㋡                    |')
    print(f'|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _| ')

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
            msg = input(" ► Fita: ")            
            tcp.send(msg.encode())
            retorno = tcp.recv(1024)
            retorno = retorno.decode()
            if retorno == "902":
                ticket(msg)
            if retorno == "904":
                time.sleep(1)
                print("\n ⚠ ⚠ ⚠ Este filme não está disponivel para locação ⚠ ⚠ ⚠ \n")
            if retorno == "906":
                time.sleep(1)
                print("\n  ⚠  Filme não encontrado... tente novamente \n")

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
        
        elif msg == "s" or msg == "sair":
            break
            
        else:
            print('\n Opção invalida... tente novamente.')
            time.sleep(2)
            pagina = 1

    except Exception as e:
        print('Erro:', e)
        print("Conexão encerrada")
tcp.close()
