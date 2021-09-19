# index method in list
numbers=[1,2,3,4,5,6,7,8,9,10]
number1=[1,2,3,4,1,5,6,7,8,1,9,10]
print(numbers.index(1))
print(number1.index(1))
print(number1.index(1,3))
print(number1.index(1,5))
print(number1.index(1,5,12))