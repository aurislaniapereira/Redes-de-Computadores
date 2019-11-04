# Import socket module 
import socket 
  
  
def Main(): 
    # local host IP '127.0.0.1' 
    host = '127.0.0.1'
  
    # Defina a porta na qual você deseja conectar 
    port = 12345
  
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
  
    # conectar ao servidor no computador local 
    s.connect((host,port)) 
  
    # mensagem que você envia ao servidor
    message = "shaurya says geeksforgeeks"
    while True: 
  
        # mensagem enviada ao servidor
        s.send(message.encode('ascii')) 
  
        # messagem recebida do servidor
        data = s.recv(1024) 
  
        # imprima a mensagem recebida 
        # aqui seria um reverso da mensagem enviada 
        print('Received from the server :',str(data.decode('ascii'))) 
  
        # pergunte ao cliente se ele quer continuar
        ans = input('\nDo you want to continue(y/n) :') 
        if ans == 'y': 
            continue
        else: 
            break
    # fecha a conexão 
    s.close() 
  
if __name__ == '__main__': 
    Main() 
