# zip() function
user_id=['user1','user2','user3']
names=['Satyam','Harshit','Abhi']
#('user1','Satyam'),('user2','Harshit'),('user3','Abhi')    #return tuple object which is itarator
print(zip(user_id,names))
print(list(zip(user_id,names)))
user_id2=['user1','user2']
names2=['Satyam','Harshit','Abhi']
print(list(zip(user_id2,names2)))
print(dict(zip(user_id2,names2)))
example=[('a',1),('b',2)]
print(dict(example))
# example of zip function
user_id=['user1','user2','user3']
first_names=['Satyam','Harshit','Abhi']
last_names=['Seth','Dixit','Yadav']
print(list(zip(user_id,first_names,last_names)))
print(dict(zip(user_id,first_names,last_names)))