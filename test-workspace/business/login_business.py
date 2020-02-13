#coding=UTF-8
from handle.login_handle import LoginHandle
'''
  po模型第三步  业务内容
  具体怎么操作
'''
class LoginBusiness():

    def __init__(self,i):
        self.login_handle = LoginHandle(i)

    def login_pass(self):
        self.login_handle.send_username('18368093836')
        self.login_handle.send_password('2121lqy53889')
        self.login_handle.click_button()


    def login_username_error(self):
        self.login_handle.send_username('18368099999')
        self.login_handle.send_password('111111111')
        self.login_handle.click_button()
        Flag = self.login_handle.get_fail_toast('账号未注册')
        if Flag:
            return True
        else:
            return False

    def login_password_error(self):
        self.login_handle.send_username('18368093836')
        self.login_handle.send_password('1111')
        self.login_handle.click_button()
        user_flag = self.login_handle.get_fail_toast('登录密码错误')
        if user_flag:
            return True
        else:
            return False

    def swipe(self):
        pass