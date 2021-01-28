from itertools import zip_longest 
print(list(zip_longest('ABCD', 'xy', fillvalue='-')))
x =[1, 2, 3, 4, 5] 
y =[8, 9]
print(list(zip_longest(x, y))) 