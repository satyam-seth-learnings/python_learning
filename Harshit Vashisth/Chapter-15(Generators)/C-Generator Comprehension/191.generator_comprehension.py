# list comprehension
square=[i**2 for i in range(1,11)]
print(square)
# generator comprehension
squares=(i**2 for i in range(1,11))
for num in squares:
    print(num)