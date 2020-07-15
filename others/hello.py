import sys

def hello1():
    if sys.argv:
        args = sys.argv
        print("hello%s\n"%args)
        print('111\n')
        print('1222\n')

if __name__ == '__main__':
    hello1()
