with open('File5.txt','r') as rf:
    with open('File5a.txt','w') as wf:
        wf.write(rf.read())