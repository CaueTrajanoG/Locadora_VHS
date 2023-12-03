import pickle
import socket
import threading
from catalogo import showCat

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
	print('Cliente: ', cliente, ' diz: ', mensagem)
	try:
		if msg == "1":
			print('Mostrar catalogo')
			showCat()
			arr = showCat()
			# conexao.send(arr)
			data_serialized = pickle.dumps(arr)
			conexao.send(data_serialized)			

	except Exception as e:
		print('Erro:', e)
		print('Mensagem invalida')



while True:    
	# Aguarda por uma conexão
    conexao, cliente = tcp.accept()
    
	# quantidade de bytes que espera receber
    # msg = conexao.recv(1024)
	
	#Recebe a conexão e inicia uma nova thread para o cliente
    threading.Thread(target=conecta_cliente, args=(conexao, cliente)).start()
conexao.close()