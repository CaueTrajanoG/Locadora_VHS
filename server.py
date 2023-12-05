import pickle
import socket
import threading
from Objects.catalogo import showCat

HOST = '0.0.0.0'  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor está
tcp = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
print('Server ON!')

tcp.listen(5) # Permite até 5 conexões pendentes

def conecta_cliente(conect, cliente):
	while True:
		msg = conect.recv(4096)
		if not msg:break		
		comunicacao(msg, conect, cliente)
	conexao.close()
	print('002', cliente)


def comunicacao(mensagem, conexao, cliente):
	msg = mensagem.decode()
	try:
		if msg == "catalogo":
			print('Mostrar catalogo')
			#Popula um array para enviar para o client
			arr = showCat()
			data_serialized = pickle.dumps(arr)
			conexao.send(data_serialized)			
		if msg == "alugar":
			msg = conexao.recv(1024)
			msg = msg.decode()
			print(f'Fita alugada: {msg.decode()}')
			confirm = "Aluguel efetuado!"
			conexao.send(confirm.encode())

	except Exception as e:
		print('Erro:', e)
		print('Mensagem invalida')



while True:    
	# Aguarda por uma conexão
    conexao, cliente = tcp.accept()
	#Recebe a conexão e inicia uma nova thread para o cliente
    threading.Thread(target=conecta_cliente, args=(conexao, cliente)).start()
conexao.close()
