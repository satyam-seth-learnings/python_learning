import os
os.chdir(r'E:\Python\Chapter-20(Python Modules)\A-OS Module\Example Folder2')
fileiter=os.walk(r'E:\Python\Chapter-20(Python Modules)\A-OS Module\Example Folder2')
for current_path,folder_names,file_names in fileiter:
    print(f'current path:{current_path}')
    print(f'folder names:{folder_names}')
    print(f'file names:{file_names}')
os.rmdir('Folder-3')
os.makedirs('Folder-4/Folder4a')