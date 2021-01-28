import itertools 
l = ['Geeks', 'for', 'Geeks'] 
iterators = itertools.cycle(l) 
for i in range(6):
	print(next(iterators), end = " ")