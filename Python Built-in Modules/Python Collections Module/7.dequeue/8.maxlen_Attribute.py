from collections import deque
de=deque([0,1,2,3],2)
print(de)
de.append(4)
print(de)
de.extend([5,6,7])
print(de)
de.insert(0,8)