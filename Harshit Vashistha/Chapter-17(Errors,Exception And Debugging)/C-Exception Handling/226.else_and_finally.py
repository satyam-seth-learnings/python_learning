# else and finally clause in exception handling
while True:
    try:
        number=int(input('Enter a number: '))
    except ValueError:
        print('Please type integer!!')
    except:
        print(f'Unexpected error!!!')
    else:
        print(f'User input={number}')
        break
    finally:
        print('Finally block....')