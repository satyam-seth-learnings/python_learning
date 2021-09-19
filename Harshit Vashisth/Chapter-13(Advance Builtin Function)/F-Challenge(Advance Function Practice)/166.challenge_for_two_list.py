# Challenge for number of list 2
def average_finder(l1,l2):
    average=[]
    for pair in zip(l1,l2):
        average.append(sum(pair)/len(pair))
    return average
print(average_finder([1,2,3],[4,5,6]))