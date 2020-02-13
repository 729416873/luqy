from appium import webdriver
import time
from util.write_user_command import WriteUserCommand

'''
   获取设备信息
'''

class BaseDriver():
    def __init__(self,i):
        self.write_user = WriteUserCommand()
        # self.deviceName = self.write_user.get_value(str(i),'deviceName')
        self.udid = self.write_user.get_value(str(i),'udid')
        self.port = self.write_user.get_value(str(i), 'port')

    def Android_driver(self):
        capabilities = {
            "platformName": "Android",
            "automationName": "UiAutomator2",  # 平台，默认Appium，为了抓取tost
            # "deviceName": "29aaf4ef",
            "deviceName": self.deviceName ,
            "app": "D:\\python\\pythonlearning\\appium\\mukewang.apk",
            #  "app":"D:\\python\\pythonlearning\\appium\\mukewang_7110.apk",#最新的app,没有登录
            # "app": "D:\\python\\pythonlearning\\appium\\gsfw-Android_standard_dev-490.apk",
            # "appWaitActivity":"cn.com.open.mooc.index.splash.MCSplashActivity",#4723
            "noReset": "true",  # 配置TRUE不是安装后首次进入页面
        }
        content = "http://127.0.0.1:"+str(self.port)+"/wd/hub"
        driver = webdriver.Remote(content , capabilities)
        time.sleep(15)
        return driver

    def Ios_driver(self):
        capabilities = {
        # 平台名称
        'platformName': 'iOS',
        # 平台版本
        'platformVersion': '13.3',#系统号
        # 设备名称
        'deviceName': 'iPhone X',#虚拟机设备型号
        "udid": self.udid ,#设备号
        "automationName": "XCUITest",
        "bundleId": "net.csdn.CsdnPlus",
        'app': '/Users/luqiuyan/luqy/CSDN 4.0.7.ipa',
        # 超时时间
        'newCommandTimeout': 30,
        # 自动化测试平台
        # 'automationName': 'Appium',
        # 是否不重新安装启动
        # 'noReset': True
        # 自动处理系统权限弹框
        # `autoAcceptAlerts`:True 低版本有效
    }

        content = "http://127.0.0.1:"+str(self.port)+"/wd/hub"
        driver = webdriver.Remote(content , capabilities)
        time.sleep(15)
        return driver

    def get_driver(self):
        pass

    def quit_driver(self):
        self.Ios_driver.quit()