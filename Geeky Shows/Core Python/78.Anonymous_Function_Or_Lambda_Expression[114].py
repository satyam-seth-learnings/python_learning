def show1(x):
    print(x)
show1(5)
show2=lambda x:print(x)
show2(5)
add=lambda  x,y:x+y
print(add(5,2))
add_sub=lambda  x,y:(x+y,x-y)
a,s=add_sub(5,2)
print(a)
print(s)
add2=lambda  x,y=1:x+y
print(add2(5,2))
print(add2(5))