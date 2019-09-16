from socket import *
serverPort = '''numero da porta do servidor'''
serverSocket = socket(AF_INET, SOCK_DGRAM)


#atribui a porta ao socket criado
serverSocket.bind(('', serverPort))
print("The server is ready to receive")
while True:
    #recebe a mensagem do cliente em bytes
    message, clientAddress = serverSocket.recvfrom(2048)
    
    #envio tbm deve ser em bytes
    serverSocket.sendto(message, clientAddress)