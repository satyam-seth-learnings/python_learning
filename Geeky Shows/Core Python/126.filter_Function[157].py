a=[10,50,60,80,90,5,45,65]
def higher_marks(n):
    if n>=60:
        return True
result1=filter(higher_marks,a)
print(result1)
print(type(result1))
for i in result1:
    print(i)
result2=list(filter(higher_marks,a))
print(result2)
print(type(result2))
for i in result2:
    print(i)
result3=list(filter(lambda n:(n>=60),a))
print(result3)
print(type(result3))
for i in result3:
    print(i)
b=[True,False,False,True,False,True]
result4=list(filter(None,b))
print(result4)
print(type(result4))
for i in result4:
    print(i)