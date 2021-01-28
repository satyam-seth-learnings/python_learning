x=[101,102,103,104,105,106,107]
print("Original List:")
n=len(x)
for  i in range(n):
    print(i,"=",x[i])
print("From 1st Position To 4th Position:")
a=x[1:5]
for i in a:
    print(i)
print("Form 0th Position To Last Position:")
b=x[0:]
for i in b:
    print(i)
print("Form 0th Position To 4th Position:")
c=x[:5]
for i in c:
    print(i)
print("Last 4 Elements:")
d=x[-4:]
for i in d:
    print(i)
print("From 0th Position To 6th Position Stride 2:")
e=x[0:7:2]
for i in e:
    print(i)
print("Last 5 Elements With [-5(-3)]=2 Elements Towards Right:")
f=x[-5:-3]
for i in f:
    print(i)