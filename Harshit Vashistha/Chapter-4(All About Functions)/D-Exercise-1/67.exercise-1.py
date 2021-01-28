def greater(num1,num2):
    if num1>num2:
        return num1
    return num2
first_num=int(input("Enter first number:"))
second_num=int(input("Enter second number:"))
print(f"{greater(first_num,second_num)} is greater")