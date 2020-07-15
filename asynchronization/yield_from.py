"""
yield from  和 @asyncio.coroutine
"""
import asyncio


@asyncio.coroutine
def main():
    print("hello")
    yield from asyncio.sleep(2)  # 阻塞直到协程sleep(2)返回结果
    print("world")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()  # 获取event_loop
    loop.run_until_complete(main())
    loop.close()
