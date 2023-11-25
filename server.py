import socket
import threading

HOST = '0.0.0.0'  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor está
tcp = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
print('Server ON!')

tcp.listen(5) # Permite até 5 conexões pendentes

def conecta_cliente(con_cli, cliente):
	print('Cliente:', cliente)
	while True:
		msg = con_cli.recv(1024)
		if not msg:break
	conexao.close()
	print('002', cliente)


while True:
    
	# Aguarda por uma conexão
    conexao, cliente = tcp.accept()
    
	# quantidade de bytes que espera receber
    msg = conexao.recv(1024)  
	
	#Recebe a conexão e inicia uma nova thread para o cliente
    threading.Thread(target=conecta_cliente, args=(conexao, cliente)).start()
     
conexao.close()