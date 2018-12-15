"""WSGI : Web Server Gateway Interface
web应用本质：
    1.浏览器发送一个HTTP请求；
    2.服务器收到请求，生成一个HTML文档；
    3.服务器把HTML文档作为HTTP响应的Body发送给浏览器；
    4.浏览器收到HTTP响应，从HTTP Body取出HTML文档并显示。
"""
# environ: 一个包含所有HTTP请求信息的dict对象；
# start_response: 一个发送HTTP响应的函数。
def application(environ, start_respose):
    start_respose('200 OK', [('Content-Type', 'text/html')])
    web = 'web'
    body = f"<h1>Hello, {environ['PATH_INFO'][1:] or web}  !</h1>"
    return [body.encode('utf-8')]