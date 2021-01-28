add=lambda x=10:(lambda y:x+y)
a=add()
print(a(20))
print(a)