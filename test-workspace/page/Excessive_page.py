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

class ExcessivePage():
    def __init__(self,i):
        base_driver = BaseDriver(i)
        # self.driver = base_driver.Android_driver()
        self.driver = base_driver.Ios_driver()
        self.get_by_local = GetByLocal(self.driver)




    def  click_tz(self):
        # 是否允许通知--不允许
        return self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name ="不允许"]')

    def is_up(self):
        # CSDN初始化页面发现新版本,点击"以后再说"
        return self.driver.tap([(55, 545), (183, 579)], 500)

    def swipe_ios(self):
        # "左滑"
        return self.driver.execute_script('mobile:swipe', {'direction': 'left'})

    def isuse(self):
        # 直接点击"立即启动"按钮
        return self.driver.tap([(147, 629), (228, 655)], 500)  # 点击立即启用

    def tuijian(self):
        # 存在"推荐"元素
        return self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="推荐"]')