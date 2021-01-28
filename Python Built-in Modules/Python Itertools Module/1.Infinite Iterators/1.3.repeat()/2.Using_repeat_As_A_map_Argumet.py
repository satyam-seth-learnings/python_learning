from itertools import repeat
print(list(map(str.upper, repeat('Satyam', 3)))) 
print(list(map(pow, range(5), repeat(2))))