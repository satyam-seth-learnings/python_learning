# Multi-level Inheritance
# Example-1
class Father:
    def showF(self):
        print('Father Class Method')
class Son(Father):
    def showS(self):
        print('Son Class Method')    
class GrandSon(Son):
    def showG(self):
        print('GrandSon Class Method')
g=GrandSon()
g.showG()
g.showS()
g.showF()
# Example-2
class Father1:
    def __init__(self):
        print('Father1 Class Constructor')
    def showF(self):
        print('Father1 Class Method')
class Son1(Father1):
    def __init__(self):
        super().__init__()
        print('Son1 Class Constructor')
    def showS(self):
        print('Son1 Class Method')    
class GrandSon1(Son1):
    def __init__(self):
        super().__init__()
        print('GrandSon1 Class Constructor')
    def showG(self):
        print('GrandSon Class Method')
g=GrandSon1()
g.showG()
g.showS()
g.showF()
