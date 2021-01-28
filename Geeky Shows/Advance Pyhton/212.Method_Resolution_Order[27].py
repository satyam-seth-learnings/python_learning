# Method Resolution Order
# Example-1
class Father:
    def __init__(self):
        super().__init__()  # Calling Parent Class Constructor
        print('Father Class Constructor')
    def showF(self):
        print('Father Class Method')
class Mother:
    def __init__(self):
        super().__init__()  # Calling Parent Class Constructor
        print('Mother Class Constructor')
    def showM(self):
        print('Mother Class Method')
class Son(Father,Mother):
    def __init__(self):
        super().__init__()  # Calling Parent Class Constructor
        print('Son Class Constructor')
    def showS(self):
        print('Son Class Method')  
s=Son()
s.showS()
s.showF()
s.showM()
# Example-2
class Son1(Mother,Father):
    def __init__(self):
        super().__init__()  # Calling Parent Class Constructor
        print('Son1 Class Constructor')
    def showS(self):
        print('Son1 Class Method')  
s1=Son1()
s1.showS()
s1.showF()
s1.showM()