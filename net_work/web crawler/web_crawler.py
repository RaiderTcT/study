import requests
import json
import urllib
r = requests.get('http://placekitten.com/g/500/600')
with open('cat_500_600.jpg', 'wb') as f:
    f.write(r.content)
url = 'https://juejin.im/entry/5976b5356fb9a06bcb7fd611'
r = requests.get(url, stream=True)
print(r.text)
print(r.content)
print(r.encoding)

# 获取来自服务器的原始套接字响应
# 确保在初始请求中设置了 stream=True
# 原始套接字可以读写内核没有处理的IP数据包，
# 而流式套接字只能读取TCP协议的数据，数据报套接字只能读取UDP协议的数据
print(r.raw.read(20))
with open ('http_file.txt', 'wb') as fd:
    # 分段写入文件，chunk_size每次获取数据的最大值
    for chunk in r.iter_content(128):
        fd.write(chunk)

# 使用 params 关键字参数，以一个字符串字典来提供这些参数
# get => params,post =>data
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get("http://httpbin.org/get", params=payload)
print(r.url)
# >>>http://httpbin.org/get?key1=value1&key2=value2&key2=value3


# 定制请求头
# 传递一个 dict 给 headers 参数
#  header 值必须是 string、bytestring 或者 unicod
url = 'https://wwww.baidu.com'
d_1 = {'user_agent': 'Mozilla/5.0'}
r = requests.get(url, headers=d_1)
print(r.url)
print(r.status_code)

# post请求, 发送一些编码为表单形式的数据
# 传递一个字典给 data 参数
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post('http://httpbin.org/post', data=payload, headers=d_1)

payload = (('key1', 'value1'), ('key1', 'value2'))
r = requests.post('http://httpbin.org/post', data=payload)
# print(r.text)

url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
headers = {'contet-type': 'application/json'}
# 接收者可以合并多个相同名称的 header 栏位，
# 把它们合为一个 "field-name: field-value" 配对，
# 将每个后续的栏位值依次追加到合并的栏位值中，
# 用逗号隔开即可，这样做不会改变信息的语义
# r = requests.post(url, data=json.dumps(payload), headers=headers)
# print(r.text)
# POST一个多部分编码(Multipart-Encoded)的文件
# rb二进制格式读取
# url = 'https://httpbin.org/post'
# files = {'files': open('report.xlsx', 'rb')}
# r = requests.post(url, files=files)
# print(r.text)
# headers 大小写不敏感
# print(r.headers)
# print(r.headers['date'])
# 4xx客户端错误和 5xx服务器错误响应，抛出异常
# Response.raise_for_status() will raise an HTTPError 
# if the HTTP request returned an unsuccessful status code.
# bad_r = requests.get('http://httpbin.org/status/404')
# bad_r.raise_for_status()

# 传递cookies给服务器
url = 'https://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print(r.text)

# cookies 以 RequestsCookiesJar的形式返回
jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')

# redirection & history 
# 除了head ，Requests会自动处理所有重定向
# response.history是一个Response对象的列表
# 按照从最老到最近的请求进行排序
r = requests.get(url, cookies=jar)
print(r.text)
r = requests.get('http://github.com')
print(r.url)
print(r.history)
