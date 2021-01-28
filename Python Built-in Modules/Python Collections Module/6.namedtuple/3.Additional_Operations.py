from collections import namedtuple
Student = namedtuple('Student',['name','age','DOB']) 
S = Student('Nandini','19','2541997') 
# using _fields to display all the keynames of namedtuple() 
print ("All the fields of students are : ") 
print (S._fields) 
# using _replace() to change the attribute values of namedtuple 
print ("The modified namedtuple is : ") 
print(S._replace(name = 'Manjeet')) 
# _field_defaults
Account = namedtuple('Account', ['type', 'balance'], defaults=[0])
print(Account._field_defaults)
print(Account('premium'))