#coding=utf-8
import time

from util.get_by_local import GetByLocal
from selenium.webdriver.support.ui import WebDriverWait#(一个class)
from selenium.webdriver.support import expected_conditions as EC#(一个条件判断，as是命名)
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver

'''
  po模型第一步  元素内容
'''

class LoginPage():
    def __init__(self,i):
        base_driver = BaseDriver(i)
        # self.driver = base_driver.Android_driver()
        self.driver = base_driver.Ios_driver()
        self.get_by_local = GetByLocal(self.driver)

    def get_username_element(self):
        '''
        获取用户名元素信息
        '''
        return self.get_by_local.get_element('username')

    def get_password_element(self):
        '''
        获取密码元素信息
        '''
        return self.get_by_local.get_element('password')

    def get_button_element(self):
        '''
        获取按钮元素信息
        '''
        return self.get_by_local.get_element('login_button')

    def get_register_element(self):
        '''
        获取注册元素信息
        '''
        return self.get_by_local.get_element('register')

    def get_forget_password_element(self):
        '''
        获取忘记密码元素信息
        '''
        return self.get_by_local.get_element('forget')

    def get_toast_element(self,message):
        '''
        获取忘记密码元素信息
        '''
        toast_element = (By.XPATH, ".//*[contains(@text,'+message+')]")
        return WebDriverWait(self.driver,10, 0.5).until(
                EC.presence_of_element_located(toast_element))


