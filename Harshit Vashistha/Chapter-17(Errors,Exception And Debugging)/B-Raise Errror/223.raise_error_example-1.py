# raise error example-1
# NotImplementedError
# abstract method
class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        raise NotImplementedError('you hove to define this method in subclasses')
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
    # def sound(self):
    #     return 'bhow bhow'
class Cat(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
    # def sound(self):
    #     return 'meao meao'
doggy=Dog('boony','pug')
print(doggy.sound())