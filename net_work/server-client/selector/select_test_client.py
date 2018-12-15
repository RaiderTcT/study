import socket

host, port = '192.168.1.101', 10001
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    # print(f'block mode:{s.getblocking()}')
    while True:
        msg = input('> ').encode('utf-8')
        if msg == b'q':
            break
        s.sendall(msg)
        data = s.recv(1024)
        print(f"Recevied {data.decode('utf-8')}")
