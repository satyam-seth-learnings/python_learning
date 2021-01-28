def disp(a,b):
    yield a
    yield b
x,y=disp(10,20)
print(x)
print(y)
result=disp(30,40)
print(result)
print(type(result))
lst=list(result)
print(lst)
print(type(lst))
result1=disp(50,60)
print(next(result1))
print(next(result1))
def show(a,b):
    while a<=b:
        yield a
        a+=1
result2=show(1,5)
print(result2)
print(type(result2))
print(next(result2))
print(next(result2))
print(next(result2))
print(next(result2))
print(next(result2))
result3=show(0,4)
print(next(result3))
print(next(result3))
for i in result3:
    print(i)