"""3.6版本后可以用async/await 将普通的函数和生成器包装成 异步生成器和异步函数
async 和 yield 可以出现在同一个函数体内
"""
import asyncio
import datetime


async def print_date(num, loop):
    end_time = loop.time() + 10.0
    while True:
        print(f"Loop:{num}, Time:{datetime.datetime.now()}")
        if (loop.time() + 1.0) >= end_time:
            break
        # 模拟的其实就是一个耗时2秒的IO读写操作。
        await asyncio.sleep(2)

loop = asyncio.get_event_loop()
tasks = [print_date(1, loop), print_date(2, loop)]
loop.run_until_complete(asyncio.gather(*tasks))
loop.close()
