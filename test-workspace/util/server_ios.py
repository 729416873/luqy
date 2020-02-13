# -*- coding: utf-8 -*-
from util.dos_cmd import DosCmd
from util.port import Port
import threading
import yaml
from util.write_user_command import WriteUserCommand
from base.base_driver import BaseDriver
import time

class Server_ios():
    '''
    对获取的设备信息再做一次处理，结果如下：
    ['127.0.0.1:62001', '127.0.0.1:62025']
    '''
    def __init__(self):
        self.dos_cmd = DosCmd()
        self.result = self.dos_cmd.execute_cmd_result('idevice_id --list')
        #['List of devices attached ', '127.0.0.1:62001\tdevice', '127.0.0.1:62025\tdevice']
        self.write_user_command = WriteUserCommand()
        self.port = Port()
        self.pport = self.port.create_port_list('4705', self.get_devices())
        self.bpport = self.port.create_port_list('4900', self.get_devices())

    def get_devices(self):
        # 处理完成后例如：['127.0.0.1:62001', '127.0.0.1:62025']
        new_result_list = []
        if len(self.result)>=1:
            for i in range(0,len(self.result)):
                new_result = self.result[i].split('\t')[0]
                new_result_list.append(new_result)
            return new_result_list
        else:
            return None



    def create_start_cmd_list(self,i):
        # ['node  /Applications/Appium.app/Contents/Resources/app/node_modules/appium/build/lib/main.js  --port 4725  --bootstrap-port  4726','']
        # main函数传入的i 决定将哪个-p、-bp和设备组合 append到list中
        cmd_list = []
        cmd = 'node  /Applications/Appium.app/Contents/Resources/app/node_modules/appium/build/lib/main.js  --port ' + str(self.pport[i]) + ' --bootstrap-port ' + str(self.bpport[i]) +' --session-override'
        cmd_list.append(cmd)

        self.write_user_command.write_command_ios(i,str(self.pport[i]),str(self.bpport[i]),str(self.get_devices()[i]))
        print(cmd_list)
        return cmd_list


    def start_server(self,i):
        # 将main函数传入的i，传给create_start_cmd_list（）

        self.dos_cmd.execute_cmd(self.create_start_cmd_list(i)[0])
        # time.sleep(5)
        # self.basedriver = BaseDriver(i)
        # self.basedriver.Android_driver()

    def kill_server(self):
        # MAC杀node.exe进程---sudo lsof -c node
        # kill -9 pid
        pass

    def main(self):
        '''
        多线程启动
        '''
        self.kill_server()
        self.write_user_command.clean_yaml()
        if self.get_devices()!=None:
            for i in range(len(self.get_devices())):
                thread = threading.Thread(target=self.start_server,args=(i,))
                thread.start()
        else:
            return None
#
# server = Server_ios()
# # # server.get_devices()
# server.main()
# # server.kill_server()