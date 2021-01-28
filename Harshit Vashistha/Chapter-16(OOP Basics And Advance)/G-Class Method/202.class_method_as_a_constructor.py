# class method as a constructor
class Person:
    count_instance=0
    def __init__(self,first_name,last_name,age):
        Person.count_instance+=1
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    @classmethod
    def from_string(cls,string):
        first,last,age=string.split(',')
        return cls(first,last,age)
    @classmethod
    def count_instances(cls):   #   class method
        return f"You have created {cls.count_instance} instances of {cls.__name__}"
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
p1=Person("Satyam","Seth",22)   # create object using init method
p2=Person("Harshit","Dixit",24) # create object using init method
p3=Person.from_string('Abhi,Yadav,25')  # create object using from_string class method
print(p3.full_name())