from itertools import chain
l1=[1,2,3]
l2=['a','b','c']
print('Approach 1:')
for i in l1+l2:
    print(i)
print('Approach 2:')
for i in chain(l1,l2):
    print(i)