
class Student():
    # 类变量
    name = 'qiyue'
    age = 0
    sum = 2
    sum1 = 777

    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(self.__class__.sum1)
        print(self.age) #在实例方法中 访问实例变量用 self.
        print(Student.sum)#在实例方法中 访问类变量 不怎么用
        print(self.__class__.sum)  # 在实例方法中 访问类变量


    def do_homework(self):
        print('homework')



student1 = Student('石敢当',18)
# 类的外部调用类变量
print(Student.sum)
# 类的外部调用实例变量
print(student1.name)




