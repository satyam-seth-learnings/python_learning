from collections import Counter 
c1 = Counter(A=4, B=3, C=10) 
c2 = Counter(A=10, B=3, C=4) 
c1.subtract(c2) 
print(c1) 