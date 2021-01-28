class Circle:
    pi=3.14 # class variable
    def __init__(self,radius):
        self.radius=radius
    def calc_circumference(self):
        return 2*Circle.pi*self.radius
c=Circle(4)
c2=Circle(5)
print(c.calc_circumference())
print(c2.calc_circumference())