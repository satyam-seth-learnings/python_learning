# create a list of squares from 1 to 10
squares=[]
for i in range(1,11):
    squares.append(i**2)
print(squares)
# using list comprehension
squares2=[i**2 for i in range(1,11)]
print(squares2)
# create a list of negative numbers from 1 to 10
negative=[]
for i in range(1,11):
    negative.append(-i)
print(negative)
# using list comprehension
new_negative=[-i for i in range(1,11)]
print(new_negative)
# example
names=['Satyam','Ankit','Harshit']
# output-new_list=['S','A','H']
new_list=[]
for name in names:
    new_list.append(name[0])
print(new_list)
# using list comprehension
new_list2=[name[0] for name in names]
print(new_list2)