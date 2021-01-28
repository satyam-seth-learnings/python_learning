# items() method
user_info={
    'name':'Satyam',
    'age':20,
    'fav_movies':['coco','kimi no na wa'],
    'fav_tunes':['awakening','fairy tele'],
}
users_items=user_info.items()
print(users_items)
print(type(users_items))
for i,j in user_info.items():
    print(f"Key is {i} and Value is {j}")
for i in user_info.items():
    print(i)