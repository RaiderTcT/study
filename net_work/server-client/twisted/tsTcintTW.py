from twisted.internet import protocol, reactor

HOST = 'localhost'
PORT = 21567


class TSClntProtocol(protocol.Protocol):
    def sendData(self):
        data = input('> ')
        if data:
            print('...sending %s ...' % data)
            self.transport.write(data.encode('utf-8'))
        else:
            # 关闭套接字-> clientConnectionLost()->停止reactor
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendData()

    def dataReceived(self, data):
        print(data.decode('utf-8'))
        self.sendData()


class TSClntFactory(protocol.ClientFactory):
    # tell base class what proto to build
    protocol = TSClntProtocol
    ClientConnectionLost = ClientConnectionFailed= \
        lambda self, connector, reason: reactor.stop()


if __name__ == '__main__':
    # 连接到tcp服务器host, port, factory, timeout=30, bindAddress=None
    # 自定义的ClientFactory类的实例对象
    reactor.connectTCP(HOST, PORT, TSClntFactory())
    reactor.run()
