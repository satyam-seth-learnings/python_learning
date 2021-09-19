# elumerate() function
names=['abc','abcdef','Satyam']
# 0 --> 'abc'
# 1 --> 'abcdef'
# 2 --> 'Satyam'
pos=0
for name in names:
    print(f"{pos} --> {name}")
    pos+=1
# with enumerate() function
for pos,name in enumerate(names):
    print(f"{pos} --> {name}")