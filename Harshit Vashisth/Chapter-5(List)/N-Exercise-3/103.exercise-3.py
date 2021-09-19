words=['abc','tuv','xyz']
def reverse_elements(l):
    elements=[]
    for i in l:
        elements.append(i[::-1])
    return elements
print(reverse_elements(words))