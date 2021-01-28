user_info={
    'name':'Satyam',
    'age':20,
    'fev_movies':['coco','kimi no na va'],
    'fev_tunes':['awakening','fairy tale'],
}
more_info={'name':'seth','State':'Uttar Pradesh','hobbies':['coding']}
user_info.update(more_info)
print(user_info)
user_info.update({})
print(user_info)