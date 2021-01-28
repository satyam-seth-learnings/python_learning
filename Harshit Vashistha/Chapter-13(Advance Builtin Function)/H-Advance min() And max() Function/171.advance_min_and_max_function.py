# advance min() and max() function
numbers=[1,2,3,4,5,6]
print(min(numbers))
print(max(numbers))
# find min and max in string according to length of string
# using function
def func(item):
    return len(item)
names=['Satyam','Zoo','Harshit','Abhi']
print(max(names))
print(max(names,key=func))
print(min(names))
print(min(names,key=func))
# using lambda expression
print(max(names,key=lambda item:len(item)))
print(min(names,key=lambda item:len(item)))
# find the name of student which has highest score from list
students={
    'Satyam':{'score':90,'age':20},
    'Harshit':{'score':75,'age':22},
    'Abhi':{'score':76,'age':24}
}
students2=[
    {'name':'Satyam','score':90,'age':20},
    {'name':'Harshit','score':75,'age':22},
    {'name':'Abhi','score':76,'age':24}
]
print(max(students2,key=lambda item:item.get('score')))
print(max(students2,key=lambda item:item.get('score'))['name'])
print(max(students2,key=lambda item:item.get('score'))['age'])
print(max(students,key=lambda item:students[item]['score']))