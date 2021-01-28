from collections import Counter 
conn=Counter('SatyamSeth')
print(conn)
print(list(conn))
print(conn['S'])
print(conn['B'])
conn['S']=0
print(conn)
del conn['S']
print(conn)