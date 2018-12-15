import asyncio
import threading
import time
"""3.6版本后可以用async/await 将普通的函数和生成器包装成 异步生成器和异步函数
async 和 yield 可以出现在同一个函数体内
"""


async def tricker(delay, to):
    """ 返回0-to， 每隔delay秒"""
    for i in range(to):
        yield i
        print(i)
        await asyncio.sleep(delay)
