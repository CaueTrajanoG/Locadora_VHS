import socket

HOST = '192.168.0.8'  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor está

# abre um socket UDP
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print('\nPara sair use CTRL+X\n')
msg = ""

while True:    
    msg = input('''
Opções:
____1- Exibir catálogo:
____2- Alugar fita:
____3- Devolver fita:
____4- Sair:
	''')
    tcp.send(msg.encode())  # str.encode devolve a string em bytes
    if msg == "4":
        break
tcp.close()