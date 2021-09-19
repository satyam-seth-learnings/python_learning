winning_number=27
user_input=int(input("Guess a number between 1 and 100 : "))
if user_input==winning_number:
    print("You Win!!!!")
else:
    if user_input<winning_number:
        print("too low")
    else:
        print("too high")