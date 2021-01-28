# Nested Class
class Army: # Outer Class
    def __init__(self):
        self.name='Rahul'
        self.gn=self.Gun()  # Creating Inner Class Object
    def show(self):
        print('Name:',self.name)
    class Gun:  # Inner Class
        def __init__(self):
            self.name='AK47'
            self.capactiy='75 Rounds'
            self.length='34.3 In'
        def disp(self):
            print('Gun Name:',self.name)
            print('Capacity:',self.capactiy)
            print('Length:',self.length)
a=Army()
print(a.name)
a.show()
print(a.gn.name)
g=a.gn
print(g.name)
g.disp()
gun=Army().Gun()    # Creating Object Of Inner Class 
print(gun.capactiy)