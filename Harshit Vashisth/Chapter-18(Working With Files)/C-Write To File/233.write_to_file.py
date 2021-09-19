# w,a,r+ mode
with open('File4.txt','w') as f:
    f.write('hello ')
with open('File4.txt','a') as f:
    f.write('my name is Khan. ')
with open('File4.txt','r+') as f:
    f.seek(len(f.read()))
    f.write('And what is your name?')