# using list comprehension
def revers_strings(l):
    return [name[::-1] for name in l]
print(revers_strings(['abc','tuv','xyz']))
# normal method
def revers_str(l):
    new_list=[]
    for name in l:
        new_list.append(name[::-1])
    return new_list
print(revers_str(['abc','tuv','xyz']))