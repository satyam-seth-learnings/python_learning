# Read Then Write
f=open('temp.txt',mode='r+')
print(f.tell())
data=f.read()
print(f.tell())
f.write('YouTube')
print(f.tell())
print(data)
print(f.tell())
f.close()
# Writing And Then Reading It Will Overwriting Existing Data
f=open('student.txt',mode='w+')
print(f.tell())
f.write('YouTube')
print(f.tell())
data=f.read()
print(f.tell())
print(data)
print(f.tell())
f.seek(0)
print(f.tell()) 
data=f.read()
print(f.tell())
print(data)
f.close()
# Appending And Then Reading It Wont Overwrite Existing Data
f=open('hello.txt',mode='a+')
print(f.tell())
f.write('Satyam Seth')
print(f.tell())
data=f.read()
print(f.tell())
print(data)
f.seek(0)
print(f.tell()) 
data=f.read()
print(f.tell())
print(data)
f.close()