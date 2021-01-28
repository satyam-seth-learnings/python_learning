a=[]
n=int(input("Enter Number Of Elements:"))
for i in range(n):
    a.append(int(input("Enter Element:")))
print(a)
print(type(a))
a=tuple(a)
print(a)
print(type(a))
print("Tuple:")
for element in a:
    print(element)