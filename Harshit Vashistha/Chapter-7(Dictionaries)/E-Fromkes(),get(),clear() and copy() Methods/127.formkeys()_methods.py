# fromkeys
# d={'name':'unknown','age':'unknown'}
d=dict.fromkeys(['name','age','hight'],'unknown')
print(d)
d=dict.fromkeys(('name','age','hight'),'unknown')
print(d)
d=dict.fromkeys("abc",'unknown')
print(d)
d=dict.fromkeys(range(1,11),'unknown')
print(d)
d=dict.fromkeys(['name','age'],['unknown','unknown'])
print(d)