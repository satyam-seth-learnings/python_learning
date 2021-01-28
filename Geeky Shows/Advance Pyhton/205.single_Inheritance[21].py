# Single Inheritance
class Father:
    money=1000
    def show(self):
        print('Parent Class Instance Method')
    @classmethod
    def showmoney(cls):
        print('Parent Class Class Method:',cls.money)
    @staticmethod
    def start():
        a=10
        print('Parent Class Static Method:',a)
class Son(Father):
    def disp(self):
        print('Child Class Instance Method')
s=Son()
s.disp()
s.show()
s.showmoney()
s.start()
Son.showmoney()
Son.start()
f=Father()
f.show()
f.showmoney()
f.start()
Father.showmoney()
Father.start()