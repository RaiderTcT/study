from contextlib import closing
import socket
import time
from threading import Thread

# 服务器在接收到


def tcplink(sock, addr):
    print('Accept new connection from %s:%s'%addr)
    # IPv 6地址
    # print('Accept new connection from %s:%s:%s:%s' % addr)
    sock.send(b'Welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        # 在接收到信息后 前面加hello后返回
        sock.send(('Hello,%s' % data.decode('utf-8')).encode('utf-8'))
    # 关闭了 新创建的套接字
    sock.close()
    print('Connection from %s:%s closed'%addr)
    # IPv 6地址
    # print('Connection from %s:%s:%s:%s' % addr)
# localhost 对应本地主机 127.0.0.1 或 ::1 
# Unix 系统下localhost比 127.0.0.1快
#  '' represents INADDR_ANY, which is used to bind to all interfaces
HOST = ''
PORT = 9999
ADDR = (HOST, PORT)

if __name__ == "__main__":
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        # 绑定监听的地址和端口, 小于1024的端口号必须要有管理员权限才能绑定
        s.bind((HOST, PORT))
        # 监听端口, 指定等待连接的最大数量
        s.listen(5)
        print('Waiting for connection...')
        print(socket.getaddrinfo(HOST, PORT))
        while True:
            # 被动接受连接，一直等待直到连接到达, 获取socket 和地址
            # 默认阻塞
            # 阻塞调用是指调用结果返回之前，当前线程会被挂起
            # 接受连接后，返回一个独立的客户端套接字
            clisock, addr = s.accept()
            print(addr)
            # 通过新的套接字，客户端服务器参与发送和接收的对话
            t = Thread(target=tcplink, args=(clisock, addr))
            t.start()
            # t.join()
