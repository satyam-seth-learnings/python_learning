from collections import UserDict 
d = {'a':1, 
	'b': 2, 
	'c': 3} 
# Creating an UserDict 
userD = UserDict(d) 
print(userD.data) 
# Creating an empty UserDict 
userD = UserDict() 
print(userD.data)