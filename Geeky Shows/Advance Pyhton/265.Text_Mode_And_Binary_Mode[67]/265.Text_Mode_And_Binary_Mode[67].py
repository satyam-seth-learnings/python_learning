f=open('student.txt',mode='w')
f.write('Hello\n')
f.write('Satyam\n')
f.write('How are you')
f.close()
print('Writing Success')
f=open('student.txt',mode='r')
data=f.read()
print(data)
f.close()
f=open('student.txt',mode='br')
data=f.read()
print(data)
f.close()