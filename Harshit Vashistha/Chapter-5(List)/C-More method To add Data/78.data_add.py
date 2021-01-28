# some more methods to add data in your list
# insert method
# how to join(concadinate) two list
# extend method
# difference between append and extend method
fruits1=['Mango','Orange']
print(fruits1)
fruits1.insert(2,"Grapes")
print(fruits1)
fruits2=['Apple','Banana']
print(fruits2)
fruits=fruits1+fruits2
print(fruits)
fruits1.extend(fruits2)
print(fruits1)
fruits2.append(fruits1)
print(fruits2)