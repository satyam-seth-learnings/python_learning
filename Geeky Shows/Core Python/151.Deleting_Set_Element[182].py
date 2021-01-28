a={10,20,'Satyam',40.25}
print("Original Set:",a)
print(id(a))
a.remove('Satyam')
print("After Removing Set:",a)
print(id(a))
# a.remove('Seth') KeyError
a.discard(20)
print("After Discarding Set:",a)
print(id(a))
a.discard('Seth')
print("After Discarding Set:",a)