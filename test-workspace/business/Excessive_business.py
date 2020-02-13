#coding=UTF-8
import time

from handle.Excessive_handle import ExcessiveHandle
'''
  po模型第三步  业务内容
  具体怎么操作
'''
class ExcessiveBusiness():

    def __init__(self,i):
        self.Excessive_handle = ExcessiveHandle(i)

    def swipe_success(self):
        self.Excessive_handle.click_tz_handle()
        time.sleep(1)
        self.Excessive_handle.click_isup()
        self.Excessive_handle.swipe()
        self.Excessive_handle.swipe()
        self.Excessive_handle.swipe()
        self.Excessive_handle.click_isuse()
        flag = True
        try:
            self.Excessive_handle.have_tuijian()
            return flag
        except:
            flag = False
            return flag