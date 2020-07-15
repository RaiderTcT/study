from urllib import request, parse

"""
URL:Uniform Resource Locator 统一资源定位符，是URI(Uniform Resource Identifier)的一部分
"""
url = "https://api.douban.com/v2/book/2129650"
with request.urlopen(url) as f:
    data = f.read()
    data_1 = data.decode('utf-8')
    print(f"Status : {f.status}, {f.reason}")
    for k, v in f.getheaders():
        print(f'{k}, {v}')
    print(f'Data: {data_1}')
    with open('douban.txt', 'wb') as t:
        t.write(data)

# 模拟发送GET请求,参数在url
req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 \
    (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print(f"Status : {f.status}, {f.reason}")
    for k, v in f.getheaders():
        print(f'{k}, {v}')
    print(f"Data: {f.read().decode('utf-8')}")

# POST请求， 参数在body
print('Login in to weibo.cn...')
username = input('>User name :')
passwd = input('>password:')
login_data = parse.urlencode([
    ('username', username),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
    ])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print(f'Status: {f.status} , {f.reason}')
    for k, v in f.getheaders():
        print(f'{k}, {v}')
    print(f"Data: {f.read().decode('utf-8')}")
