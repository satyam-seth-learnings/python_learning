# instance method
class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def is_above_18(self):
        return self.age>18
p1=Person('Harshit','Dixit',22)
p2=Person('Satyam','Seth',20)
print(p1.full_name())
print(Person.full_name(p2))
print(p1.is_above_18())
# instance method in builtin class
l1=[1,2,3,4]
l1.clear()
print(l1)
l2=[5,6,7,8]
list.clear(l2)
print(l2)
l1.append(10)
list.append(l2,10)
print(l1)
print(l2)