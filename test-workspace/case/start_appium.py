#coding=utf-8


import time
from appium import webdriver
#下面两个引入包都是为了，toast 设置智能等待
from selenium.webdriver.support.ui import WebDriverWait#(一个class)
from selenium.webdriver.support import expected_conditions as EC#(一个条件判断，as是命名)
from selenium.webdriver.common.by import By
from util.read_init import ReadIni
from util.get_by_local import GetByLocal

'''
  最初的中心思想代码
'''


def get_driver():
	# capabilities={
	# 	"platformName": "Android",
	# 	"automationName":"UiAutomator2",#平台，默认Appium，为了抓取tost
	# 	# "deviceName": "29aaf4ef",
	# 	"deviceName":"127.0.0.1:62025",
	# 	"app":"D:\\python\\pythonlearning\\appium\\mukewang.apk",
	# 	# "app":"D:\\python\\pythonlearning\\appium\\mukewang_7110.apk",#最新的app,没有登录
	# 	# "app":"D:\\python\\pythonlearning\\appium\\gsfw-Android_standard_dev-490.apk",
	# 	# "appWaitActivity":"cn.com.open.mooc.index.splash.MCSplashActivity",#4723
	# 	"noReset":"true",#配置TRUE不是安装后首次进入页面
	# }
	capabilities = {
	  "platformName": "iOS",
	  "platformVersion": "13.3",
	  "deviceName": "iPhone X",
	  "udid": "e8f3d8be3311594a9ef65cf57f9fc33e3a9c1d58",
	  "automationName": "XCUITest",
	  "bundleId": "net.csdn.CsdnPlus",
	  "app": "/Users/luqiuyan/luqy/CSDN 4.0.7.ipa",
	  # "noReset": "true"
	}
	driver = webdriver.Remote("http://127.0.0.1:4725/wd/hub",capabilities)
	time.sleep(5)
	return driver
# driver.swipe(700,400,50,400)
# driver.swipe(700,400,50,400)nox_adb.exe
def click_tz():
	#CSDN初始化页面要求选择是否通知
	time.sleep(1)
	driver.find_element_by_xpath('//XCUIElementTypeButton[@name ="不允许"]').click()
	time.sleep(2)
	#CSDN初始化页面发现新版本,点击"以后再说"
	driver.tap([(55, 545), (183, 579)], 500)

#获取屏幕的宽高
def get_size():
   size=driver.get_window_size()
   width=size['width']
   height=size['height']
   return width,height


#向左边滑动
def swipe_left():
	#[100,200]
	x1=get_size()[0]/10*9
	y1=get_size()[1]/2
	x=get_size()[0]/10
	driver.swipe(x1,y1,x,y1)


def swipe_ios():
	driver.execute_script('mobile:swipe', {'direction':'left'})
	driver.execute_script('mobile:swipe', {'direction':'left'})
	driver.execute_script('mobile:swipe', {'direction':'left'})
	driver.tap([(147, 629), (228, 655)], 500)# 点击立即启用


#向右滑动
def swipe_right():
	#[100,200]
	x1 = get_size()[0]/10
	y1 = get_size()[1]/2
	x = get_size()[0]/10*9
	driver.swipe(x1,y1,x,y1)
#向上滑动
def swipe_up():
	#[100,200]
	x1 = get_size()[0]/2
	y1 = get_size()[1]/10*9
	y = get_size()[1]/10
	driver.swipe(x1,y1,x1,y)
    #向下滑动
def swipe_down():
	#[100,200]
	x1 = get_size()[0]/2
	y1 = get_size()[1]/10
	y = get_size()[1]/10*9
	driver.swipe(x1,y1,x1,y)
def swipe_on(derection):
	if derection=='up':
		swipe_up()
	elif derection=='down':
		swipe_down()
	elif derection=='left':
		swipe_left()
	else:
		swipe_right()

def go_login():
	# print(driver.find_element_by_id('cn.com.open.mooc:id/tv_go_login'))
	driver.find_element_by_id('cn.com.open.mooc:id/tv_go_login').click()

def login():#id获取页面元素
	GetByLocal(driver).get_element('username').send_keys('18368093836')
	GetByLocal(driver).get_element('password').send_keys('2121lqy53889')
	GetByLocal(driver).get_element('login_button').click()

def login_by_class():#类获取页面元素，点击登录
	# element=driver.find_element_by_class_name('android.widget.TextView')
	# print(element)
	elements=driver.find_elements_by_class_name('android.widget.TextView')
	elements[4].click()
	# for i in elements:
	# 	i.click()
def login_by_node():#节点获取页面元素
	element=driver.find_element_by_id('cn.com.open.mooc:id/sv_scrollview')
	elements=element.find_elements_by_class_name('android.widget.EditText')
	elements[0].send_keys('11123554888')
	elements[1].send_keys('123456')
	driver.find_element_by_id('cn.com.open.mooc:id/login_lable').click()

def login_by_uiautomator():#uiautomator获取页面元素
	# driver.find_element_by_android_uiautomator('new UiSelector().text("18368029455")').clear()
	driver.find_element_by_android_uiautomator('new UiSelector().text("手机号/邮箱")').send_keys('18513199586')
	driver.find_element_by_android_uiautomator('new UiSelector().resourceId("cn.com.open.mooc:id/password_edit")').send_keys('111111')

def login_by_xpath():#xpath获取页面元素--跳转到忘记密码页面
	# driver.find_element_by_xpath('//*[contains(@text,"忘记")]').click()
	# elem=driver.find_element_by_xpath('//android.widget.TextView[@text="忘记密码"]')
	# print(elem)
	# elem.click()
	# driver.find_element_by_xpath('//android.widget.TextView[@resource-id="cn.com.open.mooc:id/login_lable"]/../preceding-sibling::android.widget.RelativeLayout').send_keys('123123')
	driver.find_element_by_xpath('//android.widget.TextView[@resource-id="cn.com.open.mooc:id/login_lable"]/../preceding-sibling::*[index="2"]').send_keys('123123')

def get_web_view():#方法2，前提把配置信息复制到appium配置框的{}内
	time.sleep(10)
	# driver.find_element_by_xpath('//android.view.View[@content-desc="Free Spire.XLS for .NET 8.3 Link"]').click()
	driver.find_element_by_accessibility_id('Free Spire.XLS for .NET 8.3 Link').click()
	driver.find_element_by_id('cn.com.open.mooc:id/left_icon').click()


def get_web_vieww():#方法1（如果只能定位到原生的webview的话可以用方法2）
	time.sleep(10)#手动操作到webview页，搜索（超链接例子）
	webview = driver.contexts
	for viw in webview:
		if 'WEBVIEW_cn.com.open.mooc' in viw:
			driver.switch_to.context(viw)
			break;
	driver.find_element_by_link_text('C').cilck()
	try:
		driver.find_element_by_id('cn.com.open.mooc:id/left_icon').click()
	except Exception as e:
		driver.switch_to.context(webview[0])
		driver.find_element_by_id('cn.com.open.mooc:id/left_icon').click()
		raise e
	print(webview)


def get_toast():
	GetByLocal(driver).get_element('username').send_keys('18368093836')
	GetByLocal(driver).get_element('login_button').click()
	#一段时间内用xpath定位文字，智能等待，用到selenium的一个包

	toast_element = (By.XPATH, ".//*[contains(@text,'请输入密码')]")
	return WebDriverWait(driver ,10, 0.5).until(
		EC.presence_of_element_located(toast_element))


driver=get_driver()
click_tz()
time.sleep(2)
swipe_ios()
# swipe_on('left')
# time.sleep(3)
# swipe_on('left')
# time.sleep(1)
# swipe_on('left')
# time.sleep(1)
# swipe_on('up')
# go_login()
# login()
# login_by_class()--点击登录
# time.sleep(2)

# login_by_node()
# login_by_uiautomator()
# login_by_xpath()--跳转到忘记密码页面
# get_toast()

