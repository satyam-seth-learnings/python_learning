from collections import ChainMap
d1={'one':1,'two':2}
d2={'three':3,'four':4}
chain=ChainMap(d1,d2)
print(chain)
print(chain.parents)