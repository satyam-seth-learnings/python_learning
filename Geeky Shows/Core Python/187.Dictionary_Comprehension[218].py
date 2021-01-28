dict1={}
for n in range(5):
    dict1[n]=n*2
print(dict1)
dict2={n:n*2 for n in range(5)}
print(dict2)
dict3={}
for n in range(10):
    if n%2==0:
        dict3[n]=n*2
print(dict3)
dict4={n:n*2 for n in range(10) if n%2==0}
print(dict4)
dict5={}
for n in range(10):
    if n%2==0:
        if n%3==0:
            dict5[n]=n*2
print(dict5)
dict6={n:n*2 for n in range(10) if n%2==0 if n%3==0}
print(dict6)
dict7={}
for n in range(5):
    if n%2==0:
        dict7[n]=n*2
    else:
        dict7[n]='Invalid'
print(dict7)
dict8={n:(n*2 if n%2==0 else 'Invalid') for n in range(5)}
print(dict8)
lst=[(101,'Rahul'),(102,'Raj')]
dict9={k:v for k,v in lst}
print(dict9)