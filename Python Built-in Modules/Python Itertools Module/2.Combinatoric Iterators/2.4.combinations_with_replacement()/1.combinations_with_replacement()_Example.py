from itertools import combinations_with_replacement  
print(list(combinations_with_replacement(['A', 2], 2)))  
print(list(combinations_with_replacement('ABC', 2)))  
print(list(combinations_with_replacement('ABC', 3)))  
print(list(combinations_with_replacement(range(2), 1)))  