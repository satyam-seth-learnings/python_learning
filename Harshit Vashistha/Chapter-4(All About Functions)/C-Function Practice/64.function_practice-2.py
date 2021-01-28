def odd_even(num):
    if num%2==0:
        return "Even Number"
    return "Odd Number"
number=int(input("Enter a number:"))
print(odd_even(number))