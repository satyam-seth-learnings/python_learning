def commonn_finder(l1,l2):
    output=[]
    for i in l1:
        if i in l2:
            output.append(i)
    return output
print(commonn_finder([1,2,3,4,8],[1,2,7,6]))