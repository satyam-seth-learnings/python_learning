a=[10,20,30,40,50]
b=a[:] # Or a.cpoy()
print("A:",a)
print("B:",b)
print("Modifying A:")
a[1]=55
print("A:",a)
print("B:",b)
print("Modifying B:")
b[2]=66
print("A:",a)
print("B:",b)