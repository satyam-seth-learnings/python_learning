from collections import OrderedDict
ud={'name':'Akash','age':21,'weight':'64Kg'}
print('Odinary Dictionary:')
for k,v in ud.items():
    print(k,v)
od=OrderedDict()
od['name']='Akash'
od['age']=21
od['weight']='64Kg'
print('OrderedDict:')
for k,v in od.items():
    print(k,v)