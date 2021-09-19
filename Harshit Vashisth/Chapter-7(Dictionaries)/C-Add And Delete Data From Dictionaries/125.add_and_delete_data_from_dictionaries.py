# add and delete data
user_info={
    'name':'Satyam',
    'age':20,
    'fev_movies':['coco','kimi no na va'],
    'fev_tunes':['awakening','fairy tale'],
}
print(user_info)
# how to add data
user_info['fev_song']=['song1','song2']
print(user_info)
# pop() method
popped_item=user_info.pop('fev_tunes')
print(f"popped item is {popped_item}")
print(type(popped_item))
print(user_info)
# popeditem() method
popped_item=user_info.popitem()
print(user_info)
print(popped_item)
print(type(popped_item))