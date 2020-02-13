#变量查找顺序：
# 1.访问实例变量 现在对象的实例变量列表中查找
# 2.没有的话去类变量中查找
# 3.若还没有去类的父类中寻找
class Student():
    # 类变量
    name = 'qiyue'
    age = 0
    sum = 1

    def __init__(self,name,age):
        # self.实例变量的名字 ——实例变量 ，用来保存类的特征值
        self.name = name
        age = age


    def do_homework(self):
        print('homework')



student1 = Student('石敢当',18)
student2 = Student('喜小乐',18)
print(student1.__dict__)
print(Student.__dict__)


