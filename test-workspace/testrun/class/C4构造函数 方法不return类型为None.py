# 1.不写ruturn内容 默认type为NoneType
# 2.构造函数只能return Nonetype 强行写个return 不是None 会报错
class Student():
    name = ''
    age = 0

    def __init__(self,name,age):
        # 构造函数
        # 初始化对象的属性
        self.name = name
        self.age = age
        print('student')
        return self.name #__init__() should return None, not 'str'

    def do_homework(self):
        print('homework')



student = Student()
a = student.__init__() #对象直接访问构造函数也可以，但一般不会这么调用
print(type(a)) #因为没有return 所以<class 'NoneType'>