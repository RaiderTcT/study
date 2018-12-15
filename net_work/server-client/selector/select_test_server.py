import socket
import selectors


class Server(object):
    def __init__(self, sel, sock):
        self.sel = sel
        self.sock = sock

    def run(self, host, port):
        self.sock.bind((host, port))
        self.sock.listen(5)
        # 设置非阻塞的socket
        self.sock.setblocking(False)
        # 注册一个文件对象,监控I/O操作
        # fileobj, events, data=None ， data是与fileobj有关的对象
        self.sel.register(self.sock, selectors.EVENT_READ, self.accept)
        while True:
            # Wait until some registered file objects become ready,
            # or the timeout expires
            # block 直到监控的socket完成
            # 返回(key, event_mask)
            # event_mask: EVENT_READ,EVENT_WRITE或组合
            # key： SelectorKey元祖
            events = self.sel.select()
            for key, mask in events:
                callback = key.data  # callback = accept
                callback(key.fileobj, mask)

    def accept(self, sock, mask):
        """接受客户端的连接，待完成后
        """
        clint_sock, addr = sock.accept()
        print('accept %s from %s' % (clint_sock, addr))
        clint_sock.setblocking(False)
        self.sel.register(clint_sock, selectors.EVENT_READ, self.read)

    def read(self, conn_sock, mask):
        data = conn_sock.recv(1024)
        if data:
            # 将对象转化为供解释器读取的形式
            print(f'echoing {repr(data)} to {conn_sock}')
            conn_sock.send(data)
        else:
            print(f'closing {conn_sock}')
            self.sel.unregister(conn_sock)
            conn_sock.close()


if __name__ == "__main__":
    sel = selectors.DefaultSelector()
    server_sock = socket.socket()
    host, port = '', 10001
    server_obj = Server(sel, server_sock)
    server_obj.run(host, port)
