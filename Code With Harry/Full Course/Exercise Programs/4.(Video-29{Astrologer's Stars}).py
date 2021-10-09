# Exercise 4
# Pattern Printing
# Input = Integer n
# Boolean = True or False
#
# True n=5
# *
# **
# ***
# ****
#
# False n=5
# ****
# ***
# **
# *
num=int(input("Enter a number:"))
bol=bool(int(input("Enter 1 Or 0:")))
if(bol==True):
    for i in range(num+1):
        for j in range(i):
            print("* ",end="")
        print("\n")
elif(bol==False):
    for i in range(num,-1,-1):
        for j in range(i):
            print("* ",end="")
        print("\n")