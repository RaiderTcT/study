from socket import *
import sys
import base64
HOST = 'localhost'
PORT = 20140
ADDR = (HOST, PORT)
BUFSIZE = 1024

while True:
    tcpClisock = socket(AF_INET, SOCK_STREAM)
    tcpClisock.connect(ADDR)
    data = input('>')
    if not data:
        break
    tcpClisock.send(bytes(data + '\n', 'utf-8'))
    data = tcpClisock.recv(BUFSIZE)
    if not data:
        break
    print(data)
    print(data.decode('utf-8'))
    # sockserver 请求处理程序的默认行为是
    # 接收连接、获取请求，然后关闭连接 
    tcpClisock.close()
