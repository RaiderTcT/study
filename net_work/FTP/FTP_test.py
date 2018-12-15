# file transport protocol

"""FTP 客户端 与 服务器端使用2个套接字进行通信（TCP）
控制和命令端口（21）
数据端口（20）
主动模式：只有在主动模式下服务器才使用数据端口，服务器把20端口设置为数据端口，它主动连接客户端的数据端口
被动模式：服务器告知客户端随机的数据端口号，客户端要主动建立数据连接
"""
import ftplib
import socket
import os
# 本机的FTP服务
HOST = '192.168.1.101'
FILE = 'timg.jpg'
UP_FILE = 'ftp_error_code.txt'


def main():

    with ftplib.FTP() as f:
        # f = ftplib.FTP()
        # f.set_debuglevel(2)
        # 
        try:
            f.connect(host=HOST)
        except socket.error as e:
            print(f'Error : can not readch {HOST}')
            return
        print(f'Connect to {HOST}')

        try:
            f.login()  # 匿名登录 user anonymous passwd
            f.dir()
        except ftplib.error_perm:
            print('Error: can not login anonymously')
            # f.quit()
            return
        try:
            f.cwd('img')  # Change to a directory
        except ftplib.error_perm:
            print("Error: can not change to doc")
            # f.quit()
            return
        print('change to directory doc')
        try:
            loc = open(FILE, 'wb')
            # 给定FTP命令，RETR filename，将一个回调函数传给retrbinary
            # 每接收到一块2进制数据都会调用本地写，创建文本
            # 传输完成后会调用loc.close()
            # self, cmd, callback, blocksize=8192, rest=None
            f.retrbinary(f'RETR {FILE}', loc.write)
        except ftplib.error_perm:
            print(f'Error: can not read flie {FILE}')
            # 下载出错则删去创建的
            os.unlink(FILE)
        else:
            print(f'Download {FILE} to cwd')
        try:
            f.cwd('../doc')
            loc = open(UP_FILE, 'rb')
            # 上传文件 STOR filename
            # self, cmd, fp, blocksize=8192, callback=None, rest=None
            f.storbinary(f'STOR {UP_FILE}', loc)
        except (FileNotFoundError) as e:
            print(f'Upload {UP_FILE} Error!')
        else:
            print(f'Upload {UP_FILE} to doc')
    # f.quit()


if __name__ == "__main__":
    main()
