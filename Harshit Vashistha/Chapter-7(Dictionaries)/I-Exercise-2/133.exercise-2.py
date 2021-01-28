user={}
name=input("What is your name:")
age=input("What is your age:")
fav_movies=input("Your fav movies seperated by comma:").split(',')
fav_songs=input("Your fav songs seperated by comma:").split(',')
user['name']=name
user['age']=age
user['fav_movies']=fav_movies
user['fav_songs']=fav_songs
for key,value in user.items():
    print(f"{key}:{value}")