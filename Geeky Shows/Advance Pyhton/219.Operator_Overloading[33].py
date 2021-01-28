# Operator Overloading
print(10+20)
print(int.__add__(10,20))
print('Satyam'+'Seth')        
print(str.__add__('Satyam','Seth'))
# Program To Add Two Objects
class A:
    def __init__(self,x):
        self.x=x
    def __add__(self,other):
        return self.x+other.x
class B:
    def __init__(self,x):
        self.x=x
a=A(100)
b=B(200)
print(a+b)
print(A.__add__(a,b))