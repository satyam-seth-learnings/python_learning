import shutil
shutil.rmtree('Example Folders1')
shutil.copytree('Example Folder2','Example Folder2/Example Folder2a')
shutil.copy('File1.txt','Example Folder2/File1a.txt')
shutil.move('File2.txt','Example Folder2/File2.txt')
shutil.move('Example Folder3','Example Folder2/Example Folder2b')