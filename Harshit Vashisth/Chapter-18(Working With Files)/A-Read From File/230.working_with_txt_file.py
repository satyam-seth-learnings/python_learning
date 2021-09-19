# read file
# open function
# read method
# seek method
# tell method
# readline method
# colse method
f=open('file1.txt')
print(f'cursor position:{f.tell()}')
print(f.read())
print('before seek method')
print(f'cursor position:{f.tell()}')
f.seek(3)
print('after seek method')
print(f'cursor position:{f.tell()}')
print(f.read())
f.seek(0)
print(f.readline())
print(f.readline(),end='')
print(f.readline())
f.seek(0)
lines=f.readlines()
print(lines)
print(len(lines))
for line in lines:
    print(line,end='')
print('\n')
print(f.closed)
print(f.name)
f.close()
print(f.closed)