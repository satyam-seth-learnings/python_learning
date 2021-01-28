from collections import deque
de=deque([0,1,2,1,3,1,4])
print(de)
c_de=de.copy()
de.clear()
print(de)
print(c_de)