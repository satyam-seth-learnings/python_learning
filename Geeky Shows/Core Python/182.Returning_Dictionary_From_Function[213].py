def show(d):
    print(d)
    print(id(d))
    print(type(d))
    for k in d:
        print(k,'=',d[k])
    return d
dc={101:'Satyam',102:'Seth'}
new_dc=show(dc)
print(new_dc)
print(id(new_dc))
print(type(new_dc))