"""
回调函数

"""
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import requests
import os
import time
from threading import currentThread


def get_page(url):

    print('%s:<%s> is getting [%s]' %
          (currentThread().getName(), os.getpid(), url))
    response = requests.get(url)
    time.sleep(2)
    return {'url': url, 'text': response.text}


def parse_page(obj):

    res = obj.result()
    print('%s:<%s> parse [%s]' %
          (currentThread().getName(), os.getpid(), res['url']))
    with open('db.txt', 'a') as f:
        parse_res = 'url:%s size:%s\n' % (res['url'], len(res['text']))
        f.write(parse_res)


if __name__ == '__main__':
    # p=ProcessPoolExecutor()
    p = ThreadPoolExecutor()
    urls = [
        'https://www.baidu.com',
        'https://www.baidu.com',
        'https://www.baidu.com',
        'https://www.baidu.com',
        'https://www.baidu.com',
        'https://www.baidu.com',
    ]

    for url in urls:
        # multiprocessing.pool_obj.apply_async(get_page,args=(url,),callback=parse_page)
        p.submit(get_page, url).add_done_callback(parse_page)
        # 与之前的回调函数拿到的结果不同，这里拿到的是前面submit方法执行完后返回的对象，要.result才能拿到对应的结果
    p.shutdown()
    print('主', os.getpid())
