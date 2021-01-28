# Constructor Overriding Without Parameter
class Father:   # Parent Class
    def __init__(self):
        self.money=1000
        print('Father Class Constructor')
    def show(self):
        print('Father Class Instance Method')
class Son(Father):
    def __init__(self):
        self.money=5000
        self.car='BMW'
    def disp(self):
        print('Son Class Instance Method')
s=Son()
print(s.money)
print(s.car)
s.disp()
s.show()
f=Father()
print(f.money)
# Constructor Overriding With Parameter
class Father1:   # Parent Class
    def __init__(self,m):
        self.money=m
        print('Father Class Constructor')
    def show(self):
        print('Father Class Instance Method')
class Son1(Father1):
    def __init__(self,r):
        self.money=r
        self.car='BMW'
    def disp(self):
        print('Son Class Instance Method')
s1=Son1(2000)
print(s1.money)
print(s1.car)
s1.disp()
s1.show()
f1=Father1(1500)
print(f1.money)