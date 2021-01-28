a={1:{'course':'Python','fees':15000},
    2:{'course':'JavaScript','fees':10000}}
print(a)
print(a[1])
print(a[1]['course'])
a[1]['course']='Java'
print(a)
del a[1]['course']
print(a)
a[1]['duration']='6 months'
print(a)
a[3]={'course':'ReactJS','fees':30000}
print(a)