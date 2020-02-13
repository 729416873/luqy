#方法 设计层面  函数：程序执行 过程式的一种称谓

class Student():
    name = ''#数据成员，用来描述类的特征
    age = 0
    def print_file(self):
        print('name:'+self.name)
        print('age:'+str(self.age))


student = Student()
student.print_file()