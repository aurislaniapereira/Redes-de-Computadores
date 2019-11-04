
import socket 
  
# importação modulo thread
from _thread import *
import threading 
  
print_lock = threading.Lock() 
  
# função thread 
def threaded(c): 
    while True: 
  
        # dados recebidos do cliente 
        data = c.recv(1024) 
        if not data: 
            print('Bye') 
              
            # bloqueio liberado na saída
            print_lock.release() 
            break
  
        # inverte a sequência especificada do cliente
        data = data[::-1] 
  
        # envia de volta a string invertida para o cliente
        c.send(data) 
  
    # fecha conexão 
    c.close() 
  
  
def Main(): 
    host = "" 
  
    # inverte uma porta no seu computador 
    # no nosso caso, é 12345
    # mas pode ser qualquer coisa 
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket ligado à porta: ", port) 
  
    # coloque o socket no modo de escuta
    s.listen(5) 
    print("socket is listening") 
  
    # loop que só para quando o cliente quiser sair
    while True: 
  
        # estabelecendo conexão com o cliente 
        c, addr = s.accept() 
  
        # bloqueio adquirido pelo cliente
        print_lock.acquire() 
        print('Connected to :', addr[0], ':', addr[1]) 
  
        # Inicie um novo thread e retorne seu identificador 
        start_new_thread(threaded, (c,)) 
    s.close() 
  
  
if __name__ == '__main__': 
    Main() 
