# Constructor With super Method
# Example-1
class Father:   # Parent Class
    def __init__(self):
        print('Father Class Constructor')
class Son(Father):
    def __init__(self):
        print('Son Class Constructor')
s=Son()
# Example-2
class Father1:   # Parent Class
    def __init__(self):
        self.money=1000
        print('Father1 Class Constructor')
class Son1(Father1):
    def __init__(self):
        super().__init__()  # Calling Parent Class Constructor
        print('Son1 Class Constructor')
    def disp(self):
        print('Son1 Class Instance Method:',self.money)
s1=Son1()
s1.disp()
# Example-3
class Father2:   # Parent Class
    def __init__(self,m):
        self.money=m
        print('Father2 Class Constructor')
class Son2(Father2):
    def __init__(self,m,j):
        self.job=j
        super().__init__(m)  # Calling Parent Class Constructor
        print('Son2 Class Constructor')
    def disp(self):
        print('Son2 Class Instance Method:',self.money,'Job:',self.job)
s2=Son2(2600,'Python')
s2.disp()