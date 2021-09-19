s={1,2,3,2,4,5}
print(s)
l=[1,2,3,1,2,5,5,5,5,4,6,7]
# remove duplicate
s2=list(set(l))
print(s2)
# add() method
s.add(7)
s.add(6)
s.add(4)
print(s)
# remove() method
s.remove(4)
s.remove(1)
print(s)
# discard() method
s.discard(3)
s.discard(9)
print(s)
# copy() method
s1=s.copy()
print(s1)
# clear() method
s.clear()
print(s)
s={1,1.0,1.1,2.33,"Satyam"}
print(s)