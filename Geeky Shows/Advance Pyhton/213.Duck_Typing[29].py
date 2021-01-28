# Duck Type
class Duck:
    def walk(self):
        print('Thapak Thapak')
class Horse:
    def walk(self):
        print('Tabdak Tabdak')
class Cat:
    def talk(self):
        print('Meow Meow')
def myfun(obj):
    obj.walk()
d=Duck()
myfun(d)
h=Horse()
myfun(h)
c=Cat()
# myfun(c)  AttributeError: 'Cat' object has no attribute 'walk'