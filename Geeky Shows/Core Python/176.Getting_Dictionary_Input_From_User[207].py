a={}
n=int(input("Number OF Elements:"))
for i in range(n):
    k=input('Enter Key:')
    v=input('Enter Value:')
    a.update({k:v})
print(a)