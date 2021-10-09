# *
# * * *
# * * * * * 
n=int(input("Enter The Number Of Rows:"))
k=1
for i in range(1,n+1):
    for j in range(1,k+1):
        print("*",end=" ")
    k+=2
    print()