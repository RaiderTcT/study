import socket

if __name__ == "__main__":
    while True:
        try:
            udpCliSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            print(socket.gethostname())
            data = input('> ')
            if data == 'q':
                break
            udpCliSock.sendto(data.encode('utf-8'), ('127.0.0.1', 9990))
            print(udpCliSock.recv(1024).decode('utf-8'))
        except KeyboardInterrupt:
            udpCliSock.close()
