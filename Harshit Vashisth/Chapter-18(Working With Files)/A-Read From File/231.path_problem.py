f=open(r'E:\Python\Chapter-18(Working With Files)\Attached Files\File2.txt')
for line in f:
    print(line,end='')
f.seek(0)
print('\n')
for line in f.readlines()[:2]:
    print(line,end='')
f.close()