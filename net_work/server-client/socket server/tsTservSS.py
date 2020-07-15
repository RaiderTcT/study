from socketserver import (TCPServer as TCP,
                          StreamRequestHandler as SRH)

from time import ctime
# 事件驱动， 包括消息的接收和发送
# SocketServer内部使用 IO多路复用 以及 “多线程” 和 “多进程” ，
# 从而实现并发处理多个客户端请求的Socket服务端。即：每个客户端请求连接到服务器时，
# Socket服务端都会在服务器是创建一个“线程”或者“进 程” 专门负责处理当前客户端的所有请求
HOST = ''
PORT = 20140
ADDR = (HOST, PORT)
# 定义一个消息、请求处理器


class MyRequestHandler(SRH):
    # 默认的handle进行任何处理
    def handle(self):
        print('...connected from ', self.client_address)
        # 使用readline方法 在客户端需要 额外的回车换行
        # StreamRequestHandler 类将输入和输出套接字看作类似文件的对象
        self.wfile.write(('[%s][%s]'%(ctime(), self.rfile.readline().decode('utf-8'))).encode('utf-8'))


if __name__ == '__main__':
    with TCP(ADDR, MyRequestHandler) as tcpServer:
        print('...Waiting for connecting...')
        tcpServer.serve_forever()
