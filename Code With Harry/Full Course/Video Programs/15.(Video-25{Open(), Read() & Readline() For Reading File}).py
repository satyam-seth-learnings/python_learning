# File IO Basics
"""
"r" Open file for reading
"w" Open a file for writting
"x" Creates file if not exists
"a" Add more content to  a file
"t" text mode
"b" binary mode
"+" read and erite
"""
#Code as discussed in the video
f = open("15.txt", "rt")
print(f.readlines())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# content = f.read()
#
# for line in f:
#     print(line, end="")
# print(content)
# content = f.read(34455)
# print("1", content)
#
# content = f.read(34455)
# print("2", content)
f.close()