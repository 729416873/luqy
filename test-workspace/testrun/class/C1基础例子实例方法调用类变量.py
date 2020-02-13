#类基本的作用：封装,且只负责定义，不负责执行
#C1 重点 在类中实例方法想调类变量，需要self.变量来访问

class Student():
    name = ''
    age = 0
    def print_file(self):
        print('name:'+self.name)#在类中实例方法想调类变量，需要self.变量来访问
        print('age:'+str(self.age))


student = Student()
student.print_file()