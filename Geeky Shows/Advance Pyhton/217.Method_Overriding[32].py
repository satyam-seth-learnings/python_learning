# Method Overriding
# Example-1
class Add:
    def result(self,a,b):
        print('Addition:',a+b)
class Multi(Add):
    def result(self,a,b):
        print('Multiplication:',a*b)
m=Multi()
m.result(10,20)
# Example-2
class Multi1(Add):
    pass
m1=Multi1()
m1.result(10,20)
# Example-3
a=Add()
a.result(10,50)