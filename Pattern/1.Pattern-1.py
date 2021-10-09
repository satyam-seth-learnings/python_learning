# *
# * *
# * * *
# * * * * 
# * * * * * 
n=int(input("Enter The Number Of Rows:"))
print("Logic-1")
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print("Logic-2")
for i in range(1,n+1):
    print("* "*i)