from numpy import *
a=array([101,102,103,104,105])
b=array([[10,20,30,40],[50,60,70,80]])
print()
# ndim Attribute
print("1D Array ndim:",a.ndim)
print("2D Array ndim:",b.ndim)
print()
# shape Attribute
# For 1D Array shape Elements In The Row
# For 2D Array shape Specifies Number Of Row And Column In Each Row
print("1D Array shape:",a.shape)
print("2D Array shape:",b.shape)
print()
# size Attribute
print("1D Array size:",a.size)
print("2D Array size:",b.size)
print()
# itemsize Attribute
print("1D Array itemsize:",a.itemsize)
print("2D Array itemsize:",b.itemsize)
print()
# dtype Attribute
print("1D Array dtype:",a.dtype)
print("2D Array dtype:",b.dtype)
print()
# nbytes Attribute
print("1D Array nbytes:",a.nbytes)
print("2D Array nbytes:",b.nbytes)
print()