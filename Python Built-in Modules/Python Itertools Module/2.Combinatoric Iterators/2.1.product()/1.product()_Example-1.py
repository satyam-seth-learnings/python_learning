from itertools import product 
print("The cartesian product using repeat:") 
print(list(product([1, 2], repeat = 2))) 
print("The cartesian product of the containers:") 
print(list(product(['Geeks', 'for', 'geeks'], '2'))) 
print("The cartesian product of the containers:") 
print(list(product('AB', [3, 4])))