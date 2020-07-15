from collections import namedtuple, deque, defaultdict, OrderedDict, Counter


class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0 
        if len(self) - containsKey >= self._capacity:
            # LIFO order if last is true or FIFO order if false.
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)



if __name__ == "__main__":

    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    print('x: %s' % p.x)
    print('y: %s' % p.y)

    # 高效实现插入和删除操作的双向列表，适合用于队列和栈

    q = deque(['a', 'b', 'c'])
    q.append('x')
    q.appendleft('z')
    print(q)
    a = q.pop()
    print(a, q)
    l = q.popleft()
    print(l, q)

    # key不存在时，返回一个默认值
    dd = defaultdict(lambda: 'N/A')
    dd['key1'] = 'abc'
    print(dd['key1'])
    print(dd['key2'])

    od = OrderedDict(a=1, b=2, c=3)
    print(od)
    # 统计字符出现个数
    c = Counter()
    for ch in 'promgraming':
        c[ch] = c[ch] + 1
    print(c)
    