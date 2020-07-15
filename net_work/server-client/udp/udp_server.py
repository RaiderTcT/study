import socket
import time
# UDP: User Datagram Protocol 用户数据报协议
if __name__ == '__main__':
    # 指定socket类型时udp
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('127.0.0.1', 9990))
    # 不需要监听，直接接收来自任何客户端的数据
    print('Bind UDP on 999...')
    while True:
        data, addr = s.recvfrom(1024)
        print('Received from %s:%s' % addr)
        print(s.gethostname())
        # 发送数据，指定地址
        s.sendto(b'[%s]Hello %s' % (time.ctime().encode('utf-8') ,data), addr)
