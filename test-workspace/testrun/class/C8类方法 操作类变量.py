
class Student():
    # 类变量
    name = 'qiyue'
    age = 0
    sum = 2
    sum1 = 777

    def __init__(self):
        # self.name = name
        # self.age = age
        self.__class__.sum1 += 1
        print(self.__class__.sum1)



    def do_homework(self):
        print('homework')

    @classmethod
    def plus_sum(cls):
        cls.sum1 +=1 #类方法中调用类变量
        print(cls.sum1)



student1 = Student()
Student.plus_sum()#类调用类方法
student1.plus_sum()#对象调用类方法（python也是可以的）

# Student.do_homework() 类不能调用实例方法
student1.do_homework()

# Student.__init__() 类不能调用构造函数
student1.__init__()



