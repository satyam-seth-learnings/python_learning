# Example-1
from abc import ABC,abstractmethod
class Father(ABC):
    @abstractmethod
    def disp(self):
        pass
# my=Father() TypeError: Can't instantiate abstract class Father with abstract methods disp
class Son(Father):
    pass
# s=Son() TypeError: Can't instantiate abstract class Son with abstract methods disp
class Child(Father):
    def disp(self):
        print('Defining Abstract Method In Child Class')
c=Child()
c.disp()
# Example-2
class One(ABC):
    @abstractmethod
    def disp1(self):
        pass
    @abstractmethod
    def disp2(self):
        pass
class Two(One):
    def disp1(self):
        print('Class Two')
        print('Disp1 Abstract Method')
# t=Two() TypeError: Can't instantiate abstract class Two with abstract methods disp2
class Three(Two):
    def disp2(self):
        print('Class Three')
        print('Disp2 Abstract Method')
th=Three()
th.disp1()
th.disp2()
# Example-3
class DefenceForce(ABC):
    @abstractmethod
    def area(self):
        pass
    def gun(self):
        pass
class Army(DefenceForce):
    def area(self):
        print('Army Area=Land')
    def gun(self):
        print('AK41')
class AirForce(DefenceForce):
    def area(self):
        print('AirForce Area=Sky')
    def gun(self):
        print('AK42')
class Navy(DefenceForce):
    def area(self):
        print('Navy Area=Sea')
    def gun(self):
        print('AK43')
a=Army()
af=AirForce()
n=Navy()
a.gun()
a.area()
af.gun()
af.area()
n.gun()
n.area()