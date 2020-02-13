#coding=utf-8
from page.Excessive_page import ExcessivePage

'''
  po模型第二步  操作内容 
  操作元素
'''

class ExcessiveHandle():
    def __init__(self,i):
        self.ExcessivePage = ExcessivePage(i)

    def click_tz_handle(self):
        self.ExcessivePage.click_tz().click()

    def click_isup(self):
        self.ExcessivePage.is_up()

    def swipe(self):
        self.ExcessivePage.swipe_ios()

    def click_isuse(self):
        self.ExcessivePage.isuse()

    def have_tuijian(self):
        self.ExcessivePage.tuijian()
