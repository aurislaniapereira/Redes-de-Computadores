from socket import * 
import select

s = socket(AF_INET, SOCK_DGRAM)
server_address = ('localhost', 12000)
mensagem = "Olá".encode()
#timeout_in_seconds = 1

#Dentro do for...
#se retornou dentro do tempo de espera
#imprime o retorno e recomeça o loop

#se nada foi retornado em 1 segundo
#assume-se que foi perdido e se reinicia o loop
for i in range(0, 10):
    s.sendto(mensagem, server_address)
    
    s.settimeout(1)
    
    try: 
        data, server = s.recvfrom(1024) 
        print(data.decode())
        continue
    except s.gettimeout: 
        print("Solicitação expirada")
        continue

s.close()
