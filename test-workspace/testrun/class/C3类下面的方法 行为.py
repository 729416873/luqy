
class Student():
    name = ''
    age = 0
    #类中的方法是描述类的行为
    def print_file(self):
        print('name:'+self.name)
        print('age:'+str(self.age))


student = Student()
student.print_file()