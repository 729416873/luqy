# -*- coding: utf-8 -*-
import yaml
import os

class WriteUserCommand():
    def read_command(self):
        '''
        打开yaml文件，返回所有内容
        '''
        current_path = os.path.abspath(os.path.dirname(__file__))
        with open(current_path+'/../config/'+'UserConfig.yaml','r') as f:
            f.seek(0)
            data = yaml.load(f.read(),Loader=yaml.FullLoader)
            # print(data)
            # print(data['userinfo1'])
            # print(data['userinfo1']['deviceName'])
            # print(data['userinfo1']['port'])
            return data

    def get_value(self,i,key = None):
        '''
        根据port bp deviceName等关键，字读取yaml中的字段信息
        :param i:
        :param key:
        :return:
        '''
        data  = self.read_command()
        userinfo = 'userinfo'+str(i)
        key_value = str(key)

        return data[userinfo][key_value]

    def write_command(self,i,port,bp,deviceName):
        '''
        将启动信息存入yaml配置文件中
        :param i:
        :param port:
        :param bp:
        :param deviceName:
        :return:
        '''
        current_path = os.path.abspath(os.path.dirname(__file__))
        with open(current_path + '/../config/' + 'UserConfig.yaml', 'a') as f: #a:追加写入 w覆盖写入
            data = {'userinfo'+str(i):
                        {'port': port,
                         'bp': bp,
                         'deviceName': deviceName}}
            yaml.dump(data,f,sort_keys=True, indent=4)

    def write_command_ios(self,i,port,bp,udid):
        '''
        将启动信息存入yaml配置文件中
        :param i:
        :param port:
        :param bp:
        :param udid:
        :return:
        '''
        current_path = os.path.abspath(os.path.dirname(__file__))
        with open(current_path + '/../config/' + 'UserConfig.yaml', 'a') as f: #a:追加写入 w覆盖写入
            data = {'userinfo'+str(i):
                        {'port': port,
                         'bp': bp,
                         'udid': udid}}
            yaml.dump(data,f,sort_keys=True, indent=4)

    def clean_yaml(self):
        current_path = os.path.abspath(os.path.dirname(__file__))
        with open(current_path + '/../config/' + 'UserConfig.yaml', 'w') as f:  # a:追加写入 w覆盖写入
            f.truncate()
        f.close()

    def get_file_lines(self):
        data = self.read_command()
        return len(data)

# write = WriteUserCommand()
#
# a = write.get_value('0','port')
# print(a)
# write.read_command()