import socket
from MySocket import MySocket
'''
服务器：
bind()
listen() :TCP
accept() :TCP
客户端:
connect() :TCP
connect_ex() :TCP
普通：
recv() :TCP
recv_into():TCP
send():TCP
sendall() :TCP
recvfrom() :UDP
recvfrom_into() :UDP
sendto() :UDP
'''
HOST = 'localhost'
# HOST = '::1'
PORT = 9999
ADDR = (HOST, PORT)
if __name__ == "__main__":
    # s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    # s.settimeout(5)
    # s.connect(ADDR)
    # print(s.recv(1024).decode('utf-8'))
    # for data in [b'Tony', b'Nick', b'Ulysses']:

    #     s.send(data)
    #     print(s.recv(1024).decode('utf-8'))

    # s.send(b'exit')
    # s.close()
    s = MySocket()
    s.connect(HOST, PORT)
    print(s.myreceive(32).decode('utf-8'))
    for data in [b'Tony', b'Nick', b'Ulysses']:
        print(len(data))
        s.mysend(data)
        print(s.myreceive(32).decode('utf-8'))
    s.mysend(b'exit')
    s.close()
