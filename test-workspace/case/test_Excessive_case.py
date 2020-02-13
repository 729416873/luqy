#coding=UTF-8
import sys
sys.path.append('/Users/luqiuyan/PycharmProjects/pythonlearning/test-workspace')
import unittest
import HTMLTestRunner
import time
import threading
import _thread
from business.Excessive_business import ExcessiveBusiness
from base.base_driver import BaseDriver
from util.server_ios import Server_ios
from multiprocessing import Process,Lock
from util.write_user_command import WriteUserCommand

'''
  单元测试内容 操作case 
'''
class NewCaseTest(unittest.TestCase):
    def __init__(self,methodName='runTest',parame=None):
        super(NewCaseTest, self).__init__(methodName)
        global Parame
        Parame = parame

class CaseTest(NewCaseTest):# 继承unittest.TestCase
    @classmethod
    def setUpClass(cls):
        global Excessive_bussiness
        Excessive_bussiness = ExcessiveBusiness(Parame)
        # basedriver = BaseDriver(Parame)
        # basedriver.Android_driver()
        # cls.a = '1234'
        # print('这是setUpClass')

    # def setUp(self):
    #     # self.a = '12345'
    #     print('这是setUp')

    @unittest.skip('CaseTest')# 不执行这个case
    def test_01(self):
        time.sleep(1)
        flag = Excessive_bussiness.swipe_success()
        self.assertTrue(flag)

        # if self.a == '1234':
        #     flag = True
        # else:
        #     flag = False
        # self.assertTrue(flag)

    # @unittest.skip('CaseTest')
    def test_02(self):
        time.sleep(1)
        flag = Excessive_bussiness.swipe_success()
        self.assertTrue(flag)

    # def test_03(self):
    #     print('这是Test03')
    #     self.assertEqual(1, 1, '相同')

    # def tearDown(self):
    #     print('这是tearDown')
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print('这是TearDownClass')

def get_suite(i):# (i,loc)进程加锁
    mutex.acquire()
    # loc.acquire() #  进程加锁
    # unittest.main()# 使用main()直接运行时，将按case的名称顺序执行
    suite = unittest.TestSuite()
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(CaseTest))# 加载用例无序

    suite.addTest(CaseTest('test_01',parame=i))

    # suite.addTest(CaseTest('test_03'))
    suite.addTest(CaseTest('test_02',parame=i))
    # unittest.TextTestRunner().run(suite)
    now = time.strftime('%Y-%m-%d %H%M%S')
    filename = '/Users/luqiuyan/PycharmProjects/pythonlearning/test-workspace/report/test_report'+str(now)+' '+str(i)+'.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp)
    runner.run(suite)
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    fp.close()
    # loc.release() 进程加锁
    mutex.release()

def get_count():
    write_user_file = WriteUserCommand()
    count = write_user_file.get_file_lines()
    return count



if __name__ == '__main__':
    server = Server_ios()
    server.main()
    time.sleep(10)
    threads = []

    # lock = Lock() 进程加锁
    mutex = _thread.allocate_lock()# 线程加锁
    def parent():
        for i in range(get_count()):
            # q = Process(target=get_suite, args=(i,lock,)) # args=(i,lock) 进程加锁
            q = _thread.start_new_thread(get_suite, (i,))
            threads.append(q)
    parent()