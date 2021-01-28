d={'name':'satyam','age':20}
d1=d.copy()
print(d1 is d)
print(d1==d)
print(d1.popitem())
print(d)
d1=d
print(d1 is d)
print(d1==d)
print(d1.popitem())
print(d)