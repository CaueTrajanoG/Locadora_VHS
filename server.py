import pickle
import socket
import threading
from Objects.catalogo import showCat,verifyDisp,verifyRent
from env import HOST, PORT

#Mutexes
mutex_alugar = threading.Semaphore(1)
mutex_devolver = threading.Semaphore(1)

tcp = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
print('  ► ► Server ON!')

tcp.listen(5) # Permite até 5 conexões pendentes

def conecta_cliente(conect, cliente):
	while True:
		msg = conect.recv(4096)
		if not msg:break		
		comunicacao(msg, conect, cliente)
	conexao.close()
	print("Cliente: ",cliente, " desconectado.")

def comunicacao(mensagem, conexao, cliente):
	msg = mensagem.decode()
	try:
		if msg == "catalogo":

			arr = showCat()
			data_serialized = pickle.dumps(arr)
			conexao.send(data_serialized)

		if msg == "alugar":

			mutex_alugar.acquire()
			msg = conexao.recv(1024)
			msg = msg.decode()
			retorno = verifyDisp(str(msg))
			mutex_alugar.release()
			conexao.send(retorno.encode())

		if msg == "devolver":

			mutex_devolver.acquire()
			msg = conexao.recv(1024)
			msg = msg.decode()
			retorno = verifyRent(str(msg))
			mutex_devolver.release()
			conexao.send(retorno.encode())

	except Exception as e:
		print('Erro:', e)
		print('Mensagem invalida')



while True:    
	# Aguarda por uma conexão
    conexao, cliente = tcp.accept()
	# Recebe a conexão e inicia uma nova thread para o cliente
    threading.Thread(target=conecta_cliente, args=(conexao, cliente)).start()
conexao.close()
