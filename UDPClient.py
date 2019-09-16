from socket import *
serverName = 'nome_do_host'


serverPort = '''numero da porta do servidor'''

clientSocket = socket(AF_INET, SOCK_DGRAM)

#a mensagem deve estar em bytes antes de ser enviada ao buffer de transmissão
clientSocket.sendto(mensagem,(serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

#devemos converter a mensagem de volta para string antes de imprimí-la
print(modifiedMessage)

#fecha a conexão
clientSocket.close()

