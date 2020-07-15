import asyncio
import threading
"""异步IO, asyncio的编程模型就是一个消息循环
3.5 后 @asyncio.coroutine -> asyncio
    yield from -> await
"""


# @asyncio.coroutine
async def hello():
    print(f"Welcome Ulysses ...{threading.current_thread()}")
    # 耗时1s的io操作
    # r = yield from asyncio.sleep(1)
    r = await asyncio.sleep(1)
    print(f'Welcome again ...{threading.current_thread()}')


# @asyncio.coroutine
async def hello_5():
    print(f"Welcome Ulysses_5 ...{threading.current_thread()}")
    # 耗时1s的io操作
    # r = yield from asyncio.sleep(5)
    r = await asyncio.sleep(5)
    print(f'Welcome again_5 ...{threading.current_thread()}')


# 异步网络连接
# @asyncio.coroutine
async def web_get(host):
    print(f"Web get from {host}...")
    # A wrapper for create_connection() returning a (reader, writer) pair.
    connect = asyncio.open_connection(host, 80)
    # reader, writer = yield from connect
    reader, writer = await connect
    header = f"GET / HTTP/1.0\r\nHost: {host}\r\n\n\n"
    # Write some data bytes to the transport.
    # This method does not block; it buffers the data and
    # arranges for it to be sent out asynchronously.
    writer.write(header.encode('utf-8'))
    # Yielding from drain() gives the opportunity for the loop to
    # schedule the write operation and flush the buffer.
    # It should especially be used
    # when a possibly large amount of data is written to the transport,
    # and the coroutine does not yield-from between calls to write().
    # yield from writer.drain()
    await writer.drain()
    while True:
        # Read one line, where “line” is a sequence of bytes ending with \n.
        # 等同于 for line in reader.readline() : yield line
        # line = yield from reader.readline()
        line = await reader.readline()
        if line == b'\r\n':
            break
        # 只显示header 部分
        print(f"{host} header > {line.decode('utf-8').rstrip()}")
    # close the transport
    writer.close()


def main():
    # loop = asyncio.get_event_loop()
    # # 两个coroutine是由同一个线程并发执行的。
    # tasks = [hello(), hello(), hello_5()]
    # # 等待协程运行完毕
    # loop.run_until_complete(asyncio.wait(tasks))
    # print(loop.is_running())
    # loop.close()
    loop = asyncio.get_event_loop()  # 1创建事件循环
    _163 = 'www.163.com'
    doc_py = 'docs.python.org'
    baidu = 'www.baidu.com'
    sina = 'www.sina.com'
    tasks = [web_get(host) for host in [doc_py, baidu, _163, sina]]
    loop.run_until_complete(asyncio.wait(tasks))  # 2 "阻塞"直到所有的tasks完成
    loop.close()  # 3 关闭循环


if __name__ == "__main__":
    main()
