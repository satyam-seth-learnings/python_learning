# exception handling
# try exception else finally
while True:
    try:
        age=int(input('Enter Your Age:'))   # seven
        break
    except ValueError:
        print('Maybe You Entered String Instead Of Number,Try Again')
    except:
        print('Unexpected Error....')
if age<10:
    print('You Can\'t Play This Game.')
else:
    print('You Can Play This Game.')