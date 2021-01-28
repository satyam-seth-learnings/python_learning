from collections import Counter 
coun = Counter()
coun.update([1, 2, 3, 1, 2, 1, 1, 2]) 
print(coun)
coun.update([1, 2, 4]) 
print(coun)