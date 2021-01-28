from collections import Counter 
# With string
c1=Counter('Allahabad')
print(c1)
# With sequence of items 
c2=Counter(['B','B','A','B','C','A','B','B','A','C']) 
print(c2)
# With dictionary 
c3=Counter({'A':3, 'B':5, 'C':2}) 
print(c3)
# With keyword arguments 
c4=Counter(A=3, B=5, C=2)
print(c4)