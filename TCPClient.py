from socket import *

serverName = 'nome_do_host'


serverPort = '''numero da porta do servidor'''


clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))


#a mensagem deve estar em bytes antes de ser enviada ao buffer de transmissão
clientSocket.send(mensagem)


#recebe a resposta do servidor
clientSocket.recv(1024)

#devemos converter a mensagem de volta para string antes de imprimí-la
print('Resposta:' , mensagem)

#fecha a conexão
clientSocket.close()