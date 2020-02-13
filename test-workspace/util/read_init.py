#目的读取localelement的信息
#coding=utf-8
#import ConfigParser--python2的导入方式
import configparser
#pip insatll ConfigParser

'''
  获取配置文件（LocalElement.ini）信息
'''

#以下是中心代码
# read_ini = configparser.ConfigParser()
# read_ini.read('D:/python/pythonlearning/test-workspace/config/LocalElement.ini')
# print(read_ini.get('login_element','username'))

#以下是封装中心代码
class ReadIni:
	# 初始化file_path和data
    def __init__(self,file_path=None):
        if file_path == None:
            self.file_path = 'D:/python/pythonlearning/test-workspace/config/LocalElement.ini'
        else:
            self.file_path = file_path
        self.data = self.read_ini()

    # 获取LocalElement.ini中信息
    def read_ini(self):
        read_ini = configparser.ConfigParser()
        read_ini.read(self.file_path)
        return read_ini

    #通过传入key和session 获取对应session中的value值
    def get_value(self,key,session = None):
        if session == None:
            self.session = 'login_element'
        else:
            self.session = session
        try:
            value = self.data.get(self.session, key)
        except :
            value = None
            return value
        else:
            return value



if __name__ == '__main__':
    read_ini= ReadIni()
    read_ini.read_ini()
    value = read_ini.get_value('username')
    print(value)
