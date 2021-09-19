# Iterator Vs Iterable
numbers=[1,2,3,4,5] #   tuples,string -----iterables
squares=map(lambda a:a**2,numbers)  #   iterator
print(next(squares))
print(next(squares))
print(next(squares))
print(next(numbers))
print(iter(numbers))