a=[10,20,30,40,50]
def inc(n):
    return n+2
result1=map(inc,a)
print(result1)
print(type(result1))
for i in result1:
    print(i)
result2=list(map(inc,a))
print(result2)
print(type(result2))
for i in result2:
    print(i)
result3=list(map(lambda  n:n+2,a))
print(result3)
print(type(result3))
for i in result3:
    print(i)
b=[1,2,3,4,5]
result4=list(map(lambda n,m:n+m,a,b))
print(result4)
print(type(result4))
for i in result4:
    print(i)