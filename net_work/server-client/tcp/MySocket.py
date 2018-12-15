import socket


class MySocket:
    def __init__(self, sock=None):
        if sock:
            self.sock = sock
        else:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        totalsent = 0
        while totalsent < len(msg):
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError('socket connection broken')
            totalsent = totalsent + sent

    def myreceive(self, bufsize):
        # chunks = []
        # bytes_recd = 0
        # while bytes_recd < bufsize:
        #     chunk = self.sock.recv(min(bufsize - bytes_recd, 2048))
        #     if chunk == b'':
        #         raise RuntimeError('socket connection broken')
        #     chunks.append(chunk)
        #     bytes_recd = bytes_recd + len(chunk)
        # return b''.join(chunks)
        return self.sock.recv(bufsize)

    def close(self):
        self.sock.shutdown()
        self.sock.close()

    def bind(self, address):
        self.sock.bind(address)

    def listen(self, backlog):
        self.sock.listen(backlog)
