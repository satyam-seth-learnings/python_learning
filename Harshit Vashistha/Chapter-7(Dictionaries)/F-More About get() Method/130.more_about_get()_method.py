# more about get() method, same keys in dictionaries
user={'name':'Satyam','age':20,'age':32}
print(user.get('name'))
print(user.get('names'))
print(user.get('names','not found!'))
print(user)