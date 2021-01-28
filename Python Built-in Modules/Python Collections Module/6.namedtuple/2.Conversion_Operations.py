from collections import namedtuple 
Student = namedtuple('Student',['name','age','DOB']) 
S = Student('Ram','19','2541997') 
li = ['Manjeet', '19', '411997' ] 
di = { 'name' : "Nikhil", 'age' : 19 , 'DOB' : '1391997' } 
print ("The namedtuple instance using iterable is : ") 
print (Student._make(li)) 
print ("The OrderedDict instance using namedtuple is : ") 
print (S._asdict()) 
print ("The namedtuple instance from dict is : ") 
print (Student(**di))