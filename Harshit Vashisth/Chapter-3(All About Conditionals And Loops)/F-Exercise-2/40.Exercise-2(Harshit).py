user_name=input("Enter your name please: ")
user_age=input("Enter your age please: ")
user_age=int(user_age)
if user_age>=10 and (user_name[0]=='a' or user_name[0]=='A'):
    print("You can watch coco")
else:
    print("You cannot watch coco")