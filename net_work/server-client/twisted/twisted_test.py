from twisted.internet import reactor
import traceback
"""
Twisted的reactor只有通过调用reactor.run()才启动。
reactor循环是在其开始的线程中运行，也就是运行在主线程中。
一旦启动，reactor就会在程序的控制下（或者具体在一个启动它的线程的控制下）一直运行下去。
reactor空转时并不会消耗任何CPU的资源。
单线程，当callback()运行时，reactor循环停止，当twisted函数停止的时候，reactor循环继续
并不需要显式的创建reactor，只需要引入,一个程序中只能有一个reactor。
"""
# 回调函数在执行的过程中，twisted的循环是被阻塞的
# 回调函数要尽快返回


def print_h():
    print('I feel not good!')


def stack():
    print('the stack')
    traceback.print_stack()


class Countdown(object):

    counter = 5

    def count(self):
        if self.counter == 0:
            reactor.stop()
        else:
            print(f'{self.counter}...')
            self.counter -= 1
            # callLater中的第二个参数是回调函数，第一个则是说明你希望在将来几秒钟时执行你的回调函数
            reactor.callLater(1, self.count)

def falldown():
    raise Exception('I fall down.')
"""Traceback (most recent call last):
  File "D:\python3.6.5\lib\site-packages\twisted\internet\base.py", line 428, in fireEvent
    DeferredList(beforeResults).addCallback(self._continueFiring)
  File "D:\python3.6.5\lib\site-packages\twisted\internet\defer.py", line 322, in addCallback
    callbackKeywords=kw)
  File "D:\python3.6.5\lib\site-packages\twisted\internet\defer.py", line 311, in addCallbacks
    self._runCallbacks()
  File "D:\python3.6.5\lib\site-packages\twisted\internet\defer.py", line 654, in _runCallbacks
    current.result = callback(current.result, *args, **kw)
--- <exception caught here> ---
  File "D:\python3.6.5\lib\site-packages\twisted\internet\base.py", line 441, in _continueFiring
    callable(*args, **kwargs)
  File "D:\study\Python Study\net work\server-client\twisted\twisted_test.py", line 38, in falldown
    raise Exception('I fall down.')
builtins.Exception: I fall down.

get up again
第一回调函数异常，第二个回调函数依然能够执行
reactor并不会因为回调函数中出现失败而停止运行
"""
def upagin():
    print('get up again')


if __name__ == "__main__":
    # reactor.callWhenRunning(ptint_h)
    # reactor.callWhenRunning(stack)
    # reactor.callWhenRunning(Countdown().count)
    reactor.callWhenRunning(falldown)
    reactor.callWhenRunning(upagin)
    reactor.run()
