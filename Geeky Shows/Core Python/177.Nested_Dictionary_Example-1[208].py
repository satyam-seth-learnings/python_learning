a={1:{},2:{}}
print(a)
print(type(a))
d={'course':'Python','fees':15000,1:{'course':'JavaScript','fees':10000}}
print(d['course'])
print(d['fees'])
print(d[1])
print(d[1]['course'])
print(d[1]['fees'])
d['course']='Machine Learning'
d[1]['fees']=200000
print(d)
del d['course']
print(d)
d['duration']='6 months'
d[1]['Name']='Satyam'
print(d)
d[2]={'course':'ReactJS','fees':30000}
print(d)