from itertools import filterfalse
li = [2, 4, 5, 7, 8] 
print (list(filterfalse(lambda x : x % 2 == 0, li))) 
print (list(filter(lambda x : x % 2 == 0, li))) 