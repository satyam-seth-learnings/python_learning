# Example-1
lst1=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
new_lst1=[]
for i in lst1:
    new_lst1.append(i+1)
print(new_lst1)
# With List Comprehension
new_lst2=[i+1 for i in lst1]
print(new_lst2)
# Example-2
new_lst3=[]
for i in range(5):
    new_lst3.append(i**2)
print(new_lst3)
# With List Comprehension
new_lst4=[i**2 for i in range(5)]
print(new_lst4)
# Example-3
lst2=[]
for i in range(20):
    if(i%2==0):
        lst2.append(i)
print(lst2)
# With List Comprehension
lst3=[i for i in range(20) if i%2==0]
print(lst3)
# Example-4
lst4=[]
for i in range(20):
    if(i%2==0):
        if(i%3==0):
            lst4.append(i)
print(lst4)
# With List Comprehension
lst5=[i for i in range(20) if i%2==0 if i%3==0]
print(lst5)
# Example-5
lst6=[]
for i in range(10):
    if(i%2==0):
        lst6.append(i)
    else:
        lst6.append('Invalid')
print(lst6)
# With List Comprehension
lst7=[i if i%2==0 else 'Invalid' for i in range(10)]
print(lst7)