import itertools 
li = [2, 4, 5, 7, 8] 
print (list(itertools.dropwhile(lambda x : x % 2 == 0, li)))
print (list(itertools.dropwhile(lambda x : x > 0, [5, 6, -8, -4, 2])))