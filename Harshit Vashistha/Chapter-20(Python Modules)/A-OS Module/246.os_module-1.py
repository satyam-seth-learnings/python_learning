# OS Module
import os
print(os.getcwd())
os.mkdir('Example-1')
# os.mkdir('Example-1')
print(os.path.exists('Example-1'))
if os.path.exists('Example-1'):
    print('already exists')
else:
    os.path.exists('Example-1')
open('File1.txt','a').close()
open('File1.txt','a').close()
os.mkdir('E:\Python\Chapter-20(Python Modules)\A-OS Module\Example Folders\Example-2')
os.chdir('E:\Python\Chapter-20(Python Modules)\A-OS Module\Example Folders\Example-2')
os.mkdir('Example-3')
print(os.listdir())
print(os.listdir('E:\Python\Chapter-20(Python Modules)\A-OS Module'))
for item in os.listdir():
    print(r'E:\Python\Chapter-20(Python Modules)\A-OS Module\Example Folders\Example-2'+'\\'+item)
for item in os.listdir():
    path=os.path.join(os.getcwd(),item)
    print(path)
for item in os.listdir(r'E:\Onlline Videos'):
    path=os.path.join(r'E:\Onlline Videos',item)
    print(path)