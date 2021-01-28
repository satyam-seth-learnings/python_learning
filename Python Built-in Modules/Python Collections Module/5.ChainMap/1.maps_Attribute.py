import collections
dic1 = { 'a' : 1, 'b' : 2 } 
dic2 = { 'b' : 3, 'c' : 4 } 
chain = collections.ChainMap(dic1, dic2) 
print ("All the ChainMap contents are : ") 
print (chain.maps)
print ("All keys of ChainMap are : ") 
print (list(chain.keys()))  
print ("All values of ChainMap are : ") 
print (list(chain.values()))