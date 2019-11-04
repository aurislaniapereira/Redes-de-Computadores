import socket, sys

if len (sys.argv) != 3 and len (sys.arq) != 2:
    print "Usage: ", sys.argv[0], " hostname [port]"
hostname = sys.argv[1]
if len (sys.argv) == 3 :
    port = int(sys.argv[2])
else:
    port = 80

READBUF = 16384
s = None

for res in socket.getaddrinfo(hostname, port, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res

    try:
        s = socket.socket(af, socktype, proto)
    except socket.error:
        s = None
        continue
    try: print "Tentando "+ sa[0]
        s.connect(sa)
    except socket.error, msg:
        s.close()
        s = None
        continue
if s :
    print "Conectado a "+sa[0]
    s.send('GET / HTTP/1.1\r\nHost:' +hostname+'\r\n\r\n')
    finished = False
    count = 0
    while not finished:
        data = s.recv(READBUF)
        count = count+1
        if len(data) != 0:
            print repr(data)
        else:
            finished = True
    s.shutdown(socket.SHUT_WR)
    s.close()
    print "Dados recebidos em ",count," chamadas" 