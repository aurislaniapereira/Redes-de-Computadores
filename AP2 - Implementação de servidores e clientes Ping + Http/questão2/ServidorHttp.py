#import socket module
from socket import *
import sys # para terminar o programa
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepara o socket servidor
HOST = 'localhost'
PORT = 8080
BUFLEN = 8192

s = socket(AF_INET, SOCK_STREAM)
try:
    print ("Iniciando HTTP server na porta ", PORT)
    s.bind((HOST, PORT, 0,0)) 
except socket.error : 
    print ("Não foi possível conectar a porta : ", PORT)
    sys.exit(-1)

s.listen(10) #máximo 10 conexões na fila


while True:
#Estabelece a conexão
    print('Ready to serve...')
    connectionSocket, addr = s._accept() 
    data = ' '
while not '\n' in data : #aguarde até que a primeira linha seja recebida 
    data = data + connectionSocket.recv(BUFLEN)
if data.startswith('GET'):

    # Solicitação GET
    connectionSocket.send('HTTP/1.0 404 NOT FOUND \r \n')
    
    # um servidor real deve mandar arquivos
else:
        #outro tipo de requisição http
        connectionSocketd.send('HTTP/1.0 501 Not implemented \r\n')

connectionSocket.send('Data: ' + now + '\r\n')
connectionSocket.send('Server: Dummy-HTTP-Server\r\n')
connectionSocket.send('\r\n')
connectionSocket.shutdown(socket.SHUT_RDWR)
connectionSocket.close()
