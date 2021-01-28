# * Operator with zip
l=[(1,2),(3,4),(5,6),(7,8)]
print(list(zip(*l)))
l1,l2=(list(zip(*l)))
print(l1)
print(l2)
print(list(l1))
print(list(l2))
L1=[1,2,5,8]
L2=[2,3,6,7]
new_list=[]
for pair in zip(L1,L2):
    new_list.append(max(pair))
print(new_list)