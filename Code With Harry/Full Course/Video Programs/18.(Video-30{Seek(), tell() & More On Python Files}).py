f = open("18.txt")
f.seek(11)
print(f.tell())
print(f.readline())
# print(f.tell())

print(f.readline())
# print(f.tell())
f.close()