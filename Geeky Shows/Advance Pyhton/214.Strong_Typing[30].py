# Strong Typing
class Duck:
    def walk(self):
        print('Thapak Thapak')
class Horse:
    def walk(self):
        print('Tabdak Tabdak')
class Cat:
    def talk(self):
        print('Meow Meow')
def myfun1(obj):
    if hasattr(obj,'walk'):
        obj.walk()
def myfun2(obj):
    if hasattr(obj,'walk'):
        obj.walk()
    if hasattr(obj,'talk'):
        obj.talk()
d=Duck()
myfun1(d)
h=Horse()
myfun1(h)
c=Cat()
myfun1(c)
myfun2(c)
myfun2(d)
myfun2(h)