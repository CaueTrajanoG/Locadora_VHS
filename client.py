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



def showMenu():
    print('''
Opções:
          +___________________+
          ||                 ||
    ► 1 - || Catálogo        ||
    ► 2 - || Alugar fita     ||
    ► 3 - || Devolver fita   ||
    ► S - || Sair            ||
          ||_________________|| 
''')

while True:    
    if pagina == 1:
        showMenu()
    msg = input()

    try:
        if msg == "catalogo":
            pagina = 2
            tcp.send(msg.encode())
            data_serialized = tcp.recv(4096)           
            data_received = pickle.loads(data_serialized)
            print("     ========================== Filmes ===========================")
            for i in range(len(data_received)):
                nome = str(data_received[i])
                nome = nome.split("|")
                print(f'    {i+1:<5} ►  {nome[0]:<60} :: {nome[2]}')
            print()
            print("voltar | sair | alugar")
        elif msg =="alugar":
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
