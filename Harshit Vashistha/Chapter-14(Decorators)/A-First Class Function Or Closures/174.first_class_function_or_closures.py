# first class function/closures
def square(a):
    return a**2
b=square(7)
print(b)
s=square
print(s(7))
print(s.__name__)
print(square.__name__)
print(s)
print(square)