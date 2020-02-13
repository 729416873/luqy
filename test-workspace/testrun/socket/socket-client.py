#encoding:utf-8
#客户端

#导入socket模块
import socket
#创建socket对象
s = socket.socket()

#连接服务端
s.connect(("127.0.0.1",4700))
data = s.recv(1024)
print(data)
# s.close()
