# Return Statement Single Value
def add(y):
    return (y+10)
sum=add(20)
print(sum)
# Return Statement Multiple Value
def cal(y):
    a=y+10
    b=y-10
    return a,b
addition,sub=cal(20)
print(addition)
print(sub)