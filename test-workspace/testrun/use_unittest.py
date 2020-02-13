#coding=UTF-8
import unittest
'''
结构
'''
class CaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('这是setUpClass')
    def setUp(self):
        print('这是setUp')
    def test_01(self):
        print('这是test01')
        self.assertNotEqual(1, 1, '相同')

    def test_02(self):
        '''
        断言
        '''
        flag = True
        print('这是Test02')
        self.assertTrue(flag)

    def tearDown(self):
        print('这是tearDown')
    @classmethod
    def tearDownClass(cls):
        print('这是TearDownClass')

if __name__ == '__main__':
    unittest.main()
