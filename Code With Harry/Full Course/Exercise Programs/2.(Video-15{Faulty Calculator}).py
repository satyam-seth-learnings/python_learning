# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result
num1=int(input("Enter the first number:"))
operator=input("Enter the operator:")
num2=int(input("Enter the sceond number:"))
def add(a,b):
    if(a==56 and b==9):
        return 77
    return (a+b)
def sub(a,b):
    return (a-b)
def mult(a,b):
    if(a==45 and b==3):
        return 555
    return (a*b)
def div(a,b):
    if(a==56 and b==6):
        return 4
    return (a/b)
if operator=="+":
    result=add(num1,num2)
elif operator=="-":
    result=sub(num1,num2)
elif operator=="*":
    result=mult(num1,num2)
elif operator=="/":
    result=div(num1,num2)
else:
    result="You entered invalid operator!"
print(f"Result:{result}")