from collections import namedtuple 
Student = namedtuple('Student',['name','age','DOB']) 
S = Student('Ram','19','2541997') 
print ("The Student age using index is : ", S[1]) 
print ("The Student name using keyname is : ",S.name) 
print ("The Student DOB using getattr() is : ",getattr(S,'DOB'))