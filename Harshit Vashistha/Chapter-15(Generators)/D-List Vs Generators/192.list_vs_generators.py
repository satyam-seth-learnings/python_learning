# list vs generators
import time
# list
t1=time.time()
l1=[i**2 for i in range(10000000)]
print(time.time()-t1)
t3=time.time()
l2=(i**2 for i in range(10000000))
print(time.time()-t3)