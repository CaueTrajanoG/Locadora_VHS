import pickle
import socket
import time
from env import HOST, PORT
from Objects.historico import print_hist
from Objects.catalogo import get_ticket_str

# abre um socket UDP
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.settimeout(1)
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

def showMenu():
    print('''
Opções:
          +___________________+
          ||                 ||
    ►     || Catálogo        ||
    ►     || Alugar          ||
    ►     || Devolver        ||
    ►     || Histórico       ||
    ►     || Sair            ||
          ||_________________|| 
''')

while True:
    if pagina == 1:
        showMenu()
    print(" ►", end=" ")
    msg = input().lower()

    try:
        if msg == "catalogo" or msg == "catálogo":
            pagina = 2
            tcp.send(msg.encode())
            data_serialized = b""
            while True:
                try:
                    packet = tcp.recv(4096)
                    if packet.decode() == "909":
                        print("Erro ao carregar o catálogo")
                        time.sleep(2)
                        pagina = 1
                        break
                    data_serialized += packet
                except socket.timeout:
                    break
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
                get_ticket_str(msg)
            if retorno == "904":
                time.sleep(1)
                print("\n ⚠ ⚠ ⚠ Este filme não está disponível para locação ⚠ ⚠ ⚠ \n")
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
            if retorno == "908":
                time.sleep(1)
                print("\n  ⚠  Filme devolvido com sucesso \n")
            if retorno == "910":
                time.sleep(1)
                print("\n  ⚠  Falha ao devolver o filme \n")
            pagina = 1
            
        elif msg == "historico":
            tcp.send(msg.encode())
            hist_data = b""
            while True:
                try:
                    packet = tcp.recv(4096)
                    hist_data += packet
                except socket.timeout:
                    break
            data_received = pickle.loads(hist_data)
            print_hist(data_received)
            pagina = 1
        
        elif msg == "s" or msg == "sair":
            break
            
        else:
            print('\n Opção inválida... tente novamente.')
            time.sleep(2)
            pagina = 1

    except Exception as e:
        print('Erro:', e)
        print("Conexão encerrada")
tcp.close()
