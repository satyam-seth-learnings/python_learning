import itertools 
GFG1 = { 5, 3, 6, 2, 1, 9 } 
GFG2 ={ 4, 2, 6, 0, 7 } 
result = itertools.accumulate(GFG2.difference(GFG1)) 
for each in result: 
	print(each) 