from itertools import starmap 
li =[(2, 5), (3, 2), (4, 3)] 
print(list(starmap(pow, li))) 
print(list(starmap(lambda x, y:x + y, li)))
print(list(starmap(min, li)))
print(list(starmap(max, li)))