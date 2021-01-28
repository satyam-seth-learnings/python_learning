from collections import defaultdict
word='SatyamSeth'
d=dict()
for char in word:
    if char not in d:
        d[char]=1
    else:
        d[char]+=1
print(d)
dd=defaultdict(int)
for char in word:
    dd[char]+=1
print(dd)