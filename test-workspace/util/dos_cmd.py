# -*- coding: utf-8 -*-
import os


class DosCmd():
    '''
    在cmd中输入command获取对应的设备信息
    简单处理一下，去掉/n
    '''
    def execute_cmd_result(self,command):#获取执行后结果
        result = os.popen(command).readlines()#popen方法相当于打印echo执行的内容
        # print(result)
        # print(result)
        #result： ['List of devices attached \n', '127.0.0.1:62001\tdevice\n', '\n']
        result_list = []
        for i in result:#为了去掉列表中的第一项
            if i == '\n':#为了去掉列表中为空的项
                continue
            new_i = i.strip("\n")
            result_list.append(new_i)
        return  result_list


    '''
    在cmd中输入command获取对应返回值
    例如Appium -p 4700 -bp 4701等
    '''
    def execute_cmd(self,command):#执行语句即可

        a = os.system(command)#system方法只返回状态0（成功）、1、2
        # print(a)
        return  a
# dos_cmd = DosCmd()
# dos_cmd.execute_cmd("taskkill /f /im node.exe")#杀死所有的appium进程
# dos_cmd.execute_cmd_result("adb devices")
# dos_cmd.execute_cmd("Appium -p 4700 -bp 4701")


if __name__ == '__main__':
    command ='ls'
    dos = DosCmd()
    dos.execute_cmd(command)