with open('temp.txt') as f:
    data=f.read()
    print(data)
    print(f.closed)
print(f.closed)