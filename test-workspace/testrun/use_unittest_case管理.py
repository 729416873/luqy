#coding=UTF-8
import unittest
'''case管理'''
class CaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('这是setUpClass')
    def setUp(self):
        print('这是setUp')

    # @unittest.skip("CaseTest")# 不执行这个case
    def test_01(self):
        print('这是test01')
    def test_02(self):
        print('这是Test02')
    def tearDown(self):
        print('这是tearDown')
    @classmethod
    def tearDownClass(cls):
        print('这是TearDownClass')

if __name__ == '__main__':
    # unittest.main()
    test_suite = unittest.TestSuite()
    test_suite.addTest('test_02')
    test_suite.addTest('test_01')

    # unittest.TextTestRunner().run(test_suite)
