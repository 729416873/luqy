# -*- coding: utf-8 -*-
from util.dos_cmd import DosCmd
import os
import socket
from util.server_ios import Server_ios
from common.common import Common

class Port_ios():
    # def __init__(self,port=None):
    #     if port == None:
    #         self.port = 4700
    #     else:
    #         self.port = port
    '''
    判断端口号是否被调用方法一
    '''
    def port_is_used(self,port):
        dos_cmd = DosCmd()
        reslut = dos_cmd.execute_cmd_result("sudo lsof -i tcp:"+str(port))
        # print(reslut)
        flag = None #为被占用
        if len(reslut)>0:
            flag = True #被占用
        else:
            flag = False
        # print(flag)
        return flag

    def create_port_list(self,start_port,device_list):
        if Common.is_unempty_list(self,device_list):
            port_list = []
            while len(device_list) != len(port_list):
                if(self.port_is_used(start_port)):
                    start_port = int(start_port)+1
                else:
                    port_list.append(str(start_port))
                    start_port = int(start_port) + 1
            # print(port_list)
            return port_list
        else:
            return  None




if __name__ =='__main__':
    port = Port_ios()
    # port.port_is_used('4725')
#     server = Server()
#     devices = server.get_devices()
    port.create_port_list('4725',['127.0.0.1:62001'])



