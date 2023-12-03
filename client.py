import pickle
import socket

HOST = '192.168.0.8'  # Endereco IP do Servidor
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
    ► 1 - || Exibir catálogo ||
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
        if msg == "1":
            pagina = 2
            tcp.send(msg.encode())
            data_serialized = tcp.recv(4096)           
            data_received = pickle.loads(data_serialized)
            print("=================== Filmes ======================")
            for i in range(len(data_received)):
                nome = str(data_received[i])
                nome = nome.split("|")
                # print(f'    {i+1} ►  {nome[0]} :: {nome[2]}')
                print(f'    {i+1:<5} ►  {nome[0]:<30} :: {nome[2]}')
            print()
            print("voltar: v | Sair: s | Alugar: numero")
            # select = input("Opção: ")
        else:
            pagina = 1

    except Exception as e:
        print('Erro:', e)
        print("Conexão encerrada")
    if msg == "s":
        break
tcp.close()
