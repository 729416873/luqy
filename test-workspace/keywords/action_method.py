# -*- coding: utf-8 -*-
from util.get_by_local import GetByLocal
from base.base_driver import BaseDriver
import time
import ast

class ActionMethod:
    def __init__(self):
        self.basedriver = BaseDriver(0)#先传个0 简单点用于调试
        self.driver = self.basedriver.Android_driver()
        self.get_by_local = GetByLocal(self.driver)

    def input(self,*args):
        '''
        根据页面元素和操作值进行操作
        :param element_key:取LocalElement.ini,通过调用get_by_local.py
        :param value:
        :return:
        '''
        input_element = self.get_by_local.get_element(args[0])
        if input_element == None:
            raise Exception("没有找到对应元素",input_element)
        if args[1] == None:
            raise Exception("没有找到对应操作值", args[1])
        input_element.send_keys(args[1])

    def onclick(self,*args):
        onclick_element = self.get_by_local.get_element(args[0])
        if onclick_element == None:
            raise Exception("没有找到对应元素",onclick_element)
        else:
            onclick_element.click()

    def sleep(self,*args):
        time.sleep(args[0])


    def get_size(self):
        self.size = self.driver.get_window_size()
        width = self.size['width']
        height = self.size['height']
        return width, height


    # 向左边滑动
    def swipe_left(self):
        # [100,200]
        x1 = self.get_size()[0] / 10 * 9
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10
        self.driver.swipe(x1, y1, x, y1)


    # 向右滑动
    def swipe_right(self):
        # [100,200]
        x1 = self.get_size()[0] / 10
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10 * 9
        self.driver.swipe(x1, y1, x, y1)


    # 向上滑动
    def swipe_up(self):
        # [100,200]
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10 * 9
        y = self.get_size()[1] / 10
        self.driver.swipe(x1, y1, x1, y)
        # 向下滑动


    def swipe_down(self):
        # [100,200]
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10
        y = self.get_size()[1] / 10 * 9
        self.driver.swipe(x1, y1, x1, y)


    def swipe_on(self,derection):
        if derection == 'up':
            self.swipe_up()
        elif derection == 'down':
            self.swipe_down()
        elif derection == 'left':
            self.swipe_left()
        else:
            self.swipe_right()

    def tap_point(self,position,duration=None):
        # self.driver.tap([(147, 629), (228, 655)], 500)
        list_list = ast.literal_eval(position)#'list'转换成list
        self.driver.tap(list_list,duration)
