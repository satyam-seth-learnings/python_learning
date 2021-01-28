a={'course':'Python','fees':15000,1:{'course':'JavaScript','fees':10000}}
for i in a:
    print(i)
for i in a:
    if type(a[i]) is dict:
        for k in a[i]:
            print(k,'=',a[i][k])
    else:
        print(i,'=',a[i])