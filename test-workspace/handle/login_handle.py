#coding=utf-8
from page.login_page import LoginPage

'''
  po模型第二步  操作内容 
  操作元素
'''

class LoginHandle():
    def __init__(self,i):
        self.loginpage = LoginPage(i)

    def send_username(self,message):
        self.loginpage.get_username_element().send_keys(message)

    def send_password(self,message):
        self.loginpage.get_password_element().send_keys(message)

    def click_button(self):
        self.loginpage.get_button_element().click()

    def click_forget_password(self):
        self.loginpage.get_forget_password_element().click()

    def click_register(self):
        self.loginpage.get_register_element().click()

    def get_fail_toast(self,message):
        '''
        根据是否获取到对应toast信息返回True or False
        '''
        toast_element = self.loginpage.get_toast_element(message)
        if toast_element:
            return True
        else:
            return False
