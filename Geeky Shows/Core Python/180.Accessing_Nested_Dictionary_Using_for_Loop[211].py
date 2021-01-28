a={1:{'course':'Python','fees':15000},
    2:{'course':'JavaScript','fees':10000}}
print("ID:")
for id in a:
    print(id)
for id in a:
    for k in a[id]:
        print(k,'=',a[id][k])