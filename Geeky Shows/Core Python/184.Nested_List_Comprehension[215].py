a=[[24,30,36],[28,35,42]]
print(a)
l=[]
for i in range(6,8):
    temp=[]
    for j in range(4,7):
        temp.append(i*j)
    l.append(temp)
print(l)
lst=[[i*j for j in range(4,7)] for i in range(6,8)]
print(lst)