# self不是关键字，他其实是可以替换成其他的，但是关键字是不可变的
#类变量 与 实例变量
class Student():
    # 类变量
    name = 'qiyue'
    age = 0
    sum = 1

    def __init__(self,name,age):
        # self.实例变量的名字 ——实例变量 ，用来保存类的特征值
        self.name = name # 特征值只和对象相关，与类无关
        self.age = age


    def do_homework(self):
        print('homework')



student1 = Student('石敢当',18)
student2 = Student('喜小乐',18)
print(student1.name)#对象.name
print(student2.name)
print(Student.name)#类.name

