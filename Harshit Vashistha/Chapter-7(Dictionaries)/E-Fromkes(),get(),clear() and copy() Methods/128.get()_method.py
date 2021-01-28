# get() method
d={'name': 'Satyam', 'age': 20, 'hight': 'unknown'}
print(d['name'])
# print(d['names']) ~Error
print(d.get('name'))
print(d.get('names'))
if 'names' in d:
    print('present')
else:
    print('not present')
if d.get('names'):
    print('present')
else:
    print('not present')