numbers=list(range(1,11))
def square(l):
    square_list=[]
    for i in l:
        square_list.append(i**2)
    return square_list
print(square(numbers))