import itertools 
li = [2, 4, 6, 7, 8, 10, 20] 
iti = iter(li) 
it = itertools.tee(iti, 3) 
print ("The iterators are : ") 
for i in range (0, 3): 
	print (list(it[i]))