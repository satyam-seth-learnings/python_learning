# Example-1
from abc import ABC,abstractmethod
class Father(ABC):
    @abstractmethod
    def disp(self):
        pass
    def show(self):
        print('Concrete Method')
# my=Father() TypeError: Can't instantiate abstract class Father with abstract methods disp
class Child(Father):
    def disp(self):
        print('Defining Abstract Method In Child Class')
c=Child()
c.disp()
c.show()
# Example-2
class DefenceForce(ABC):
    def __init__(self):
        self.id=101
    @abstractmethod
    def area(self):
        pass
    def gun(self):
        print('Gun=AK47')
class Army(DefenceForce):
    def area(self):
        print('Army Area=Land',self.id)
class AirForce(DefenceForce):
    def area(self):
        print('AirForce Area=Sky',self.id)
class Navy(DefenceForce):
    def area(self):
        print('Navy Area=Sea',self.id)
a=Army()
af=AirForce()
n=Navy()
a.gun()
a.area()
af.gun()
af.area()
n.gun()
n.area()