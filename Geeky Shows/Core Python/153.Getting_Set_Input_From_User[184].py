a=set()
print(id(a))
n=int(input("Enter Number Of Elements:"))
for i in range(n):
    el=input("Enter Element:")
    a.add(el)
print(a)
print(id(a))