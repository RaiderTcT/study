import hashlib, random

md5 = hashlib.md5()
# 只接受 bytes-like objects (normally bytes) 
# m.update(a), m.update(b)  等价于 m.update(a+b)
md5.update('this is a test of hashlib.'.encode('utf-8'))
# hexdiget() 16进制返回， digest是 bytes object
print(md5.hexdigest())
md5.update('this is a test of hashlia.'.encode('utf-8'))
print(md5.hexdigest())
sha1 = hashlib.sha1()
sha1.update('this is a test of hashlib.'.encode('utf-8'))
sha1.update('python hashlib.'.encode('utf-8'))
print(sha1.hexdigest())


def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)


db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}


def login(username, password):
    if username in db.keys():
        user = db[username]
        md5 = get_md5(password + user.salt)
        print('md5', md5)
        print('user password md5:', user.password)
        return md5 == user.password
    return False


# if __name__ == "__main__":

#     assert login('michael', '123456')
#     assert login('bob', 'abc999')
#     assert login('alice', 'alice2008')
#     assert not login('michael', '1234567')
#     assert not login('bob', '123456')
#     assert not login('alice', 'Alice2008')