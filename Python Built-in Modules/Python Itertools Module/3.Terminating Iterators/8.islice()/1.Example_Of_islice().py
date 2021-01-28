from itertools import islice
print(list(islice('ABCDEFG', 2)))
print(list(islice('ABCDEFG', 2, 4)))
print(list(islice('ABCDEFG', 2, None)))
print(list(islice('ABCDEFG', 0, None, 2)))