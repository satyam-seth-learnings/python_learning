# with block
# context maneger
with open('File3.txt') as f:
    data=f.read()
    print(data)
print(f.closed)