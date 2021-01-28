# class method
# difference between class and instance method
class Person:
    count_instance=0
    def __init__(self,first_name,last_name,age):
        Person.count_instance+=1
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    @classmethod
    def count_instances(cls):   #   class method
        return f"You have created {cls.count_instance} instances of {cls.__name__}"
p1=Person("Satyam","Seth",22)
p2=Person("Harshit","Dixit",24)
print(Person.count_instances())
print(p2.count_instances())