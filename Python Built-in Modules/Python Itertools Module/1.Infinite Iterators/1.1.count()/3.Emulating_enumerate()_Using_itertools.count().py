from itertools import count
my_list =["Geeks", "for", "Geeks"] 
for i in zip(count(start = 1,step = 1), my_list): 
	print(i) 