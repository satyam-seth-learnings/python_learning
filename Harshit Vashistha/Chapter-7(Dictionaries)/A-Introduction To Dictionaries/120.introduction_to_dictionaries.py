# introduction to dictionaries
user={'Name':'Satyam','Age':20}
print(user)
print(type(user))
user1=dict(Name='Satyam',Age=20)
print(user1)
print(type(user1))
print(user['Name'])
print(user1['Age'])
user_info={
    'name':'Satyam',
    'age':20,
    'fav_movies':['coco','kimi no na wa'],
    'fav_tunes':['awakening','fairy tele'],
}
print(user_info['fav_movies'])
user_info2={}
user_info2['Name']='Satyam'
user_info2['Age']=20
print(user_info2)