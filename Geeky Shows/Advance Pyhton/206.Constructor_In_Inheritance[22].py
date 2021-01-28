# Example-1
class Father:
    def __init__(self):
        self.money=2000
        print('Father Class Constructor')
    def show(self):
        print('Father Class Instance Method')
class Son(Father):
    def disp(self):
        print('Son Class Instance Method')
s=Son()
print(s.money)
s.show()
s.disp()
class Father1:
    def __init__(self,m):
        self.money=m
        print('Father1 Class Constructor')
    def show(self):
        print('Father1 Class Instance Method')
class Son1(Father1):
    def disp(self):
        print('Son1 Class Instance Method',self.money)
s1=Son1(1000)
print(s1.money)
s1.show()
s1.disp()