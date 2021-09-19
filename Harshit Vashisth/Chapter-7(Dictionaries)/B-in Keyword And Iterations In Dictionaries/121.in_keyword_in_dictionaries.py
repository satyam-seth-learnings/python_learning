# in keyword in dictionaries
user_info={
    'name':'Satyam',
    'age':20,
    'fav_movies':['coco','kimi no na wa'],
    'fav_tunes':['awakening','fairy tele'],
}
# check if key exist in dictionaries
if 'name' in user_info:
    print("present")
else:
    print("not prsesent")
# check if value exist in dictionaries
if 24 in user_info.values():
    print("present")
else:
    print("not prsesent")
if ['coco','kimi no na wa'] in user_info.values():
    print("present")
else:
    print("not prsesent")