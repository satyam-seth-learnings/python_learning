from itertools import chain 
l1=[1,2,3]
l2=['a','b','c']
lit=[l1,l2]
print (list(chain.from_iterable(lit)))
li =['ABC', 'DEF', 'GHI'] 
res1 = list(chain(li)) 
res2 = list(chain.from_iterable(li)) 
print("Using chain :", res1)
print("Using chain.from_iterable :", res2) 