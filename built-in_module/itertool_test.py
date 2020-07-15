import itertools

cs = itertools.repeat('abc', 5)
for c in cs:
    print(c)
natuals = itertools.count(1)
# 判断来截取出一个有限的序列

ns = itertools.takewhile(lambda x: x < 20, natuals)

print(list(ns))

for c in itertools.chain('abc', '123'):
    print(c, end=' ')
print('')

for key, group in itertools.groupby('aa1111bbccaaa'):
    print(key, list(group))

for key, group in itertools.groupby('Aa1111bbCcaAa', lambda x: x.upper()):
    print(key, list(group))

def pi(N):
    chain = itertools.count(0)
    odd_chain = itertools.takewhile(lambda x: x < N, chain)
    new_list = [(2*x+1) for x in odd_chain]
    result =[4 / new_list[i] * (1 if i%2 == 0 else -1) for i in  range(len(new_list))]
    return sum(result)
if __name__ == "__main__":
    l1 = list(range(10))
    l2 = list(range(10))
    print(pi(10))
    print(pi(100))
    print(pi(1000))
    print(pi(10000))