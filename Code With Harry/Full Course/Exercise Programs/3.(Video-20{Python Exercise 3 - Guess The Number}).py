num=50
guesses=4
i=0
while(guesses!=0):
    usernum=int(input("Guess the number:"))
    if(usernum>num):
        print("Number is too low")
        guesses-=1
        i+=1
    elif(usernum<num):
        print("Number is too high")
        guesses-=1
        i+=1
    elif(usernum==num):
        i+=1
        break
if(guesses==0):
        print("Game Over!")
else:
    print("You enter the same number.")
    print(f"Total number of gusses is {i}")