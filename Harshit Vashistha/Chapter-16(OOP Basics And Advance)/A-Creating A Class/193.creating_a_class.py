# Objects
# class
# creating a class
# init method/constructor
# attribute,instance variable
# creatin our objects
class Person:
    def __init__(self,first_name,last_name,age):
        # inctance variable
        print('init method / constructor get called')
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
p1=Person('Satyam','Seth',22)
p2=Person('Harshit','Dixit',24)
print(p1.first_name)
print(p2.first_name)