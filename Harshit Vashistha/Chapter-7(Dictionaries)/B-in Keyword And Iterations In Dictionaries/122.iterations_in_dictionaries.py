# loops in dictionaries
user_info={
    'name':'Satyam',
    'age':20,
    'fav_movies':['coco','kimi no na wa'],
    'fav_tunes':['awakening','fairy tele'],
}
for i in user_info:
    print(i)
for i in user_info:
    print(user_info[i])
for i in user_info.values():
    print(i)
for i in user_info.keys():
    print(i)