# Hierarchical Inheritance
# Example-1
class Father:
    def showF(self):
        print('Father Class Method')
class Son(Father):
    def showS(self):
        print('Son Class Method')    
class Daughter(Father):
    def showD(self):
        print('Daughter Class Method')    
s=Son()
s.showS()
s.showF()
d=Daughter()
d.showD()
d.showF()
# Example-2
class Father1:
    def __init__(self):
        print('Father1 Class Constructor')
    def showF(self):
        print('Father1 Class Method')
class Son1(Father1):
    def __init__(self):
        print('Son1 Class Constructor')
    def showS(self):
        print('Son1 Class Method')    
class Daughter1(Father1):
    def __init__(self):
        super().__init__()
        print('Daughter1 Class Constructor')
    def showD(self):
        print('Daughter1 Class Method')    
s1=Son1()
s1.showS()
s1.showF()
d1=Daughter1()
d1.showD()
d1.showF()