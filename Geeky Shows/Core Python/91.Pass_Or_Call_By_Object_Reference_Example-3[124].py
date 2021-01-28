def val(lst):
    print("IFBA",lst,id(lst))
    lst=[11,22,33]
    print("IFAA",lst,id(lst))
lst=[1,2,3]
print("BCF",lst,id(lst))
val(lst)
print("ACF",lst,id(lst))