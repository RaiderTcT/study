from wsgiref.simple_server import make_server
from WSGI_hello import application
# ddd
# 创建服务器， 处理函数为application
httpd = make_server('', 8000, application)
print('Servering HTTP on port 8000...')
httpd.serve_forever()
