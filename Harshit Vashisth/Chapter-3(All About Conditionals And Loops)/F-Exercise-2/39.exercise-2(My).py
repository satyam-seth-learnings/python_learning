name,age=input("Enter comma separated name and age: ").split(",")
if name.lower()[0]=='a' and int(age)>10:
    print("You can watch coco movie")
else:
    print("Sorry,You connot watch coco")