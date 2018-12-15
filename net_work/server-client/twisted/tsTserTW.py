from twisted.internet import protocol, reactor
from time import ctime
# 类似socket server的事件驱动网络框架
PORT = 21567


class TSServProtocol(protocol.Protocol):
    # 客户端连接服务器时，执行
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print(f'...connected from:{clnt}...')
    # 服务器接收到客户端发送的数据
    def dataReceived(self, data):
        self.transport.write(
            f"[{ctime()}] {data.decode('utf-8')}".encode('utf-8'))


if __name__ == "__main__":
    # 创建协议工厂，每次得到一个接入连接时，都能制造协议的一个实例
    factory = protocol.Factory()
    factory.protocol = TSServProtocol
    print('...Waiting for connection...')
    # reactor 安装一个TCP监听器，检测服务请求
    # 当接收到一个请求时，创建一个TSServProtocol实例
    reactor.listenTCP(PORT, factory)
    reactor.run()
