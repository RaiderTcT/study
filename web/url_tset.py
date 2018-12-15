from urllib import request, parse, error
"""url 的构成 prot_sch://net_loc/path;params?query#frag
    网络协议、下载方案://服务器所在地/文件或CGI应用路径;可选参数?连接符（&）分割的一系列键值对#指定文档内特定锚的部分
    https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen
    https://www.baidu.com/s?
    ie=utf-8&f=3&rsv_bp=0&rsv_idx=1&tn=baidu&wd=urllib3&rsv_pq=89b04eec0001974f&rsv_t=4199EL0OqHZgikOVBhMgZexypVR1jG7TbPZbfg%2FozSvVF%2B7KFV4ieA8DnnY&rqlang=cn&rsv_enter=1&rsv_sug3=1&rsv_sug1=1&rsv_sug7=001&rsv_sug2=1&rsp=0&rsv_sug9=es_1_1&rsv_sug4=1540&rsv_sug=9
    net_loc:   user:passwd@host:port
"""
# CGI(Common Gateway Interface)CGI 应用程序能与浏览器进行交互,还可通过数据库API 与数据库服务器等外部数据源进行通信,从数据库服务器中获取数据
# parse 解析url
url = 'http://www.w3school.com.cn/html5/index.asp'
o = parse.urlparse(url)
print(o)
print(f"scheme: {o.scheme}, port: {o.port}, fragment: {o.fragment}, url: {o.geturl()}")
print(f"urlunparse: {parse.urlunparse(o)}")
with request.urlopen(url) as f:
    # 返回MIME : Multipurpose Internet Mail Extension头文件
    print(f.info())
    print(f.fileno())
    # print(f.read().decode('utf-8'))
# 将HTML文件下载到本地中
filename, mime_hdrs = request.urlretrieve(
    url, filename=r'd:/study/Python study/web/html5_s.html')
print(f'file: {filename}')
# 指定file方案 打开本地文件
# url = r'file:D:/study/Python Study/web/git_command.txt'
# with request.urlopen(url) as f:
#     print(f.read().decode('utf-8'))


# quote 将不能打印的字符或非web有效字符 转化
name = 'ulysses wu'
number = 6
base = 'http://www/~foo/cgi-bin/s.py'
final = f'{base}?name={name}num={number}'
print(f'Origin: {final}')
urldata = parse.quote(final)
print(f'quote: {urldata}')
print(f'unquote:{parse.unquote(urldata)}')

# urlencode() ,接收键值对，并编译成字符串
login_data = parse.urlencode([
    ('username', 'jack'),
    ('password', '123'),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', '')])
print(login_data)

LOGIN = 'Ulysses'
PASSWD = ''
URL = 'http://localhost'
# 认证域
REALM = 'Secure Archive'


def handler_version(url):
    hdlr = request.HTTPBasicAuthHandler()
    hdlr.add_password(REALM,
                      parse.urlparse(url)[1], LOGIN, PASSWD)
    opener = request.build_opener(hdlr)
    # ...and install it globally so it can be used with urlopen.
    request.install_opener(opener)
    return url


def request_version(url):
    from base64 import encodestring
    req = request.Request(url)
    b64str = encodestring(bytes(f'{LOGIN}:{PASSWD}', 'utf-8'))[:-1]
    req.add_header("Authorization", f'Basic {b64str}')
    return req

for funcType in ('handler', 'request'):
    print(f'***Using {funcType.upper()}***')
    url = eval(f'{funcType}_version')(URL)
    f = request.urlopen(url)
    print(str(f.readline(), 'utf-8'))
    f.close()
