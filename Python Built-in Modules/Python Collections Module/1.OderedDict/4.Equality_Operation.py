from collections import OrderedDict
ud1={'name':'Akash','age':21,'weight':'64Kg'}
ud2={'age':21,'weight':'64Kg','name':'Akash'}
print('Ordinary Dictionary:',ud1==ud2)
od1=OrderedDict()
od1['name']='Akash'
od1['age']=21
od1['weight']='64Kg'
od2=OrderedDict()
od2['age']=21
od2['weight']='64Kg'
od2['name']='Akash'
print('OrderedDict:',od1==od2)