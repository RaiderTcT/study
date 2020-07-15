import socket
from contextlib import closing
# TCP : Transmission Control Protocl 传输控制协议
# 指定使用IPv4协议， AF_INET6： IPv6协议； 面向流的TCP协议
with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 参数为元组（地址， 端口号）80为web服务的标准端口
    s.connect(('www.baidu.com', 80))
    # 发送数据，请求返回首页数据
    s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')
    buffer = []
    while True:

        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
    data = b''.join(buffer)
# s.close()
# 分隔header 和html
header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
print(header.decode('utf-8'))
with open('baidu.html', 'wb') as f:
    f.write(html)
