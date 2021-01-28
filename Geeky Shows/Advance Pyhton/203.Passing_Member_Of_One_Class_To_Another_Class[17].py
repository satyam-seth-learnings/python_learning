# Passing Members Of One Class To Another Class
class Student:
    # Constructor
    def __init__(self,n,r):
        self.name=n
        self.roll=r
    # Instance Method
    def disp(self):
        print('Student Name:',self.name)
        print('Student Roll:',self.roll)
class User:
    # Static Method
    @staticmethod
    def show(s):
        print('User Name:',s.name)
        print('User Roll:',s.roll)
        s.disp()
# Creating Object Of Student Class
stu=Student('Satyam',101)
User.show(stu)