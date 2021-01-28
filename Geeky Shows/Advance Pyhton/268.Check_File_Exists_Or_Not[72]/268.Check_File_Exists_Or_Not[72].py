from os.path import isfile
if isfile('name.txt'):
    f=open('name.txt')
    print('File Oppend')
    f.close()
else:
    print('File Not Found')