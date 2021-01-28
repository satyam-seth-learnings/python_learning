a=(10,20,30,40,50)
b=a
print("A:",a)
print("ID of A:",id(a))
print("B:",b)
print("ID of B:",id(b))
a=a[:3]
print(a)
print(id(a))
print(b)
print(id(b))