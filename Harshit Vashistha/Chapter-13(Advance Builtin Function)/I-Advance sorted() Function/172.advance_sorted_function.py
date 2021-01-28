# Advance sort() method and sorted() function
# sort() method with list
fruits=['graeps','mango','apple']
fruits.sort()
print(fruits)
# sorted() function with tuple
fruits2=('graeps','mango','apple')
print(sorted(fruits))
# sorted() function with set
fruits3={'graeps','mango','apple'}
print(sorted(fruits3))
# Example 
smartphones=[
    {'Model':'S6','Price':24000},
    {'Model':'Note5','Price':18000},
    {'Model':'S8','Price':45000}
]
print(sorted(smartphones,key=lambda d:d['Price']))
print(sorted(smartphones,key=lambda d:d['Price'],reverse=True))
sorted_smartphones=(sorted(smartphones,key=lambda d:d['Price'],reverse=True))
print(sorted_smartphones)