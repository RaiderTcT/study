import threading
import time

class MyThread(threading.Thread):
    def __init__(self, func, name, args):
        super().__init__()
        self.name = name
        self.func = func
        self.args = args

    def getResult(self):
        return self.res

    def run(self):
        print(f'{self.name} starting at {time.ctime()}')
        self.res = self.func(*self.args)
        print(f"{self.name} finished at {time.ctime()}")
