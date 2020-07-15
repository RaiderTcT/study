import unittest
from MyDict import MyDict

"""
断言语法    解释
assertEqual(a, b)   判断a==b
assertNotEqual(a, b)    判断a！=b
assertTrue(x)   bool(x) is True
assertFalse(x)  bool(x) is False
assertIs(a, b)  a is b
assertIsNot(a, b)    a is not b
assertIsNone(x)  x is None
assertIsNotNone(x)  x is not None
assertIn(a, b)  a in b
assertNotIn(a, b)   a not in b
assertIsInstance(a, b)  isinstance(a, b) 
assertNotIsInstance(a, b)   not isinstance(a, b)
"""

# 从unittest.TestCase类继承，创建一个测试类
class TestMyDict(unittest.TestCase):

    def setUp(self):
        print('setup..')

    def tearDown(self):
        print('teardown')

    # 测试方法以test开头
    def test_init(self):
        d = MyDict(a=2, b="3")
        self.assertEqual(d.a, 2)
        self.assertEqual(d.b, '3')

    def test_key(self):
        d = MyDict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = MyDict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    # 期待抛出指定类型的Error
    def test_keyerror(self):
        d = MyDict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = MyDict()
        with self.assertRaises(AttributeError):
            value = d.empty


if __name__ == "__main__":

    unittest.main()
