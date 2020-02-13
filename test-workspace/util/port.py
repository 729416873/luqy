# -*- coding: utf-8 -*-
from util.dos_cmd import DosCmd
import os
import socket
# from util.server import Server
from common.common import Common

class Port():
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
        reslut = dos_cmd.execute_cmd_result("netstat -ano|findstr "+str(port))
        # print(reslut)
        flag = None #为被占用
        if len(reslut)>0:
            flag = True #被占用
        else:
            flag = False
        return flag

    '''
        判断端口号是否被调用方法二
    '''
    def IsUsed(self,port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind(('127.0.0.1', int(port)))
            s.close()
            # 利用shutdown()函数使socket双向数据传输变为单向数据传输。shutdown()需要一个单独的参数，
            # 该参数表示了如何关闭socket。具体为：0表示禁止将来读；1表示禁止将来写；2表示禁止将来读和写。
            # print('%s 未被占用' % port)
            return False
        except Exception as e:
            print('str(e):\t\t', str(e))
            # print('%s 被占用' % port)
            return True

    def create_port_list(self,start_port,device_list):
        if Common.is_unempty_list(self,device_list):
            port_list = []
            while len(device_list) != len(port_list):
                if(self.IsUsed(start_port)):
                    start_port = int(start_port)+1
                else:
                    port_list.append(str(start_port))
                    start_port = int(start_port) + 1
            # print(port_list)
            return port_list
        else:
            return  None




if __name__ =='__main__':
    port = Port()
#     server = Server()
#     devices = server.get_devices()
    port.create_port_list('4701',['127.0.0.1:62001'])



