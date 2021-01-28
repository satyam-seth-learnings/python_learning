# Example-1
set1={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19}
new_set1=set()
for i in set1:
    new_set1.add(i+1)
print(new_set1)
print(type(new_set1))
# With Set Comprehension
new_set2={i+1 for i in set1}
print(new_set2)
print(type(new_set2))
# Example-2
new_set3=set()
for i in range(5):
    new_set3.add(i**2)
print(new_set3)
# With Set Comprehension
new_set4={i**2 for i in range(5)}
print(new_set4)
# Example-3
set2=set()
for i in range(20):
    if(i%2==0):
        set2.add(i)
print(set2)
# With Set Comprehension
set3={i for i in range(20) if i%2==0}
print(set3)
# Example-4
set4=set()
for i in range(20):
    if(i%2==0):
        if(i%3==0):
            set4.add(i)
print(set4)
# With Set Comprehension
set5={i for i in range(20) if i%2==0 if i%3==0}
print(set5)
# Example-5
set6=set()
for i in range(10):
    if(i%2==0):
        set6.add(i)
    else:
        set6.add(-i)
print(set6)
# With Set Comprehension
set7={i if i%2==0 else -i for i in range(10)}
print(set7)