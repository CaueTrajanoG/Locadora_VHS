import pickle
import socket
import threading
from Objects.catalogo import showCat,verifyDisp,verifyRent
from Objects.historico import get_all_hist, increment_hist
from env import HOST, PORT
from structures.Exceptions import CatalogoException, AluguelException, DevolucaoException,FilmeException

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
			try:
				arr = showCat()
				data_serialized = pickle.dumps(arr)
				conexao.send(data_serialized)
				arr.clear()
			except:
				mensagem = '909' 	# 909 > Erro ao carregar o catálogo
				conexao.send(mensagem.encode())

		if msg == "alugar":  
			msg = conexao.recv(1024)
			msg = msg.decode()

			mutex_alugar.acquire()

			try:
				verifyDisp(str(msg))
				retorno = '902' 	# 902 > SUCESSO AO ALUGAR
			except AluguelException:
				retorno = '904' 	# 904 > NÃO FOI POSSIVEL ALUGAR
			except FilmeException:
				retorno = '906' 	# 906 > FILME NÃO ENCONTRADO
			
			mutex_alugar.release()
			
			if retorno == '902':
				increment_hist(cliente, str(msg))
			conexao.send(retorno.encode())

		if msg == "devolver":
			msg = conexao.recv(1024)
			msg = msg.decode()
			try:
				if verifyRent(str(msg)):
					retorno = '908' 	#908 > FILME DEVOLVIDO COM SUCESSO
					conexao.send(retorno.encode())
			except DevolucaoException:
				mensagem = '910'		#910 > NÃO FOI POSSIVEL DEVOLVER O FILME
				conexao.send(mensagem.encode())

		if msg == "historico":
			# buscamos o histórico do cliente e enviamos ao client
			hist = get_all_hist(cliente)
			data_serialized = pickle.dumps(hist)
			conexao.send(data_serialized)

	except Exception as e:
		print('Erro:', e)


while True:    
	# Aguarda por uma conexão
    conexao, cliente = tcp.accept()
	# Recebe a conexão e inicia uma nova thread para o cliente
    threading.Thread(target=conecta_cliente, args=(conexao, cliente)).start()
conexao.close()
