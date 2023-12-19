import pickle
import socket
import threading
from Objects.catalogo import showCat,verifyDisp,verifyRent
from Objects.historico import get_all_hist, increment_hist
from env import HOST, PORT
from structures.Exceptions import CatalogException

#Mutexes
mutex_alugar = threading.Semaphore(1)


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
		if msg == "catalogo" or msg == "catálogo":

			#RC
			try:
				arr = showCat()
				data_serialized = pickle.dumps(arr)
				conexao.send(data_serialized)
				arr.clear()
			except:
				# 909 > Erro ao carregar o catálogo
				mensagem = '909'
				conexao.send(mensagem.encode())

		if msg == "alugar":

			msg = conexao.recv(1024)
			msg = msg.decode()

			#RC
			mutex_alugar.acquire()
			retorno = verifyDisp(str(msg))
			mutex_alugar.release()
			
			if retorno == '902':
				increment_hist(cliente, str(msg))
			conexao.send(retorno.encode())

		if msg == "devolver":
			msg = conexao.recv(1024)
			msg = msg.decode()

			#RC
			retorno = verifyRent(str(msg))

			conexao.send(retorno.encode())
   
		if msg == "historico":
			hist = get_all_hist(cliente)
			data_serialized = pickle.dumps(hist)
			conexao.send(data_serialized)


	except Exception as e:
		print('Erro:', e)
		print('Mensagem invalida')



while True:    
	# Aguarda por uma conexão
    conexao, cliente = tcp.accept()
	# Recebe a conexão e inicia uma nova thread para o cliente
    threading.Thread(target=conecta_cliente, args=(conexao, cliente)).start()
conexao.close()
