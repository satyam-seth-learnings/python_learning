from collections import Counter
c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
print(c + d)                       # add two counters together:  c[x] + d[x]
print(c - d)                       # subtract (keeping only positive counts)
print(c & d)                       # intersection:  min(c[x], d[x]) 
print(c | d)                       # union:  max(c[x], d[x])