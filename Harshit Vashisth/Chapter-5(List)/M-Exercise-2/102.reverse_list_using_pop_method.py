# reverse list using pop method
numbers=list(range(1,11))
def reverse_list(l):
    r_list=[]
    for i in range(len(l)):
        r_list.append(l.pop())
    return r_list
print(reverse_list(numbers))