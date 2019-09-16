from socket import *

serverPort = '''numero da porta do servidor'''

serverSocket = socket(AF_INET, SOCK_STREAM)

#atribui a porta ao socket criado
serverSocket.bind(('', serverPort))

#aceita conexões com no máximo um cliente na fila
serverSocket.listen(1)

print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    
    #recebe a mensagem do cliente em bytes
    mensagem = connectionSocket.recv(1024).decode()
    
    #envio tbm deve ser em bytes
    connectionSocket.send(mensagem)
    
    connectionSocket.close()