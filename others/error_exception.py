# err_logging.py

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('1')
    except ZeroDivisionError as e:
        logging.exception(e)
        raise ValueError('input error!')
        # 打印完错误信息后，继续运行

main()
print('END')