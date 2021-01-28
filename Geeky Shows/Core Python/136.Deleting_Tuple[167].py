a=(10,-50,21.3,'Satyam')
print(a)
tup1=a[0:3]
print(tup1)
print(id(a))
print(id(tup1))
s1=a[0:2]
s2=a[3:]
tup2=s1+s2
print(tup2)
# del a[1] TypeError: 'tuple' object doesn't support item deletion
del a
# print(a)    NameError: name 'a' is not defined