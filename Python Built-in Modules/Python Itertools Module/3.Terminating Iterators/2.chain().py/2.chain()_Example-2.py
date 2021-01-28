from itertools import chain 
res = list(chain('ABC', 'DEF', 'GHI')) 
print(res) 
str1 ="Geeks"
str2 ="for"
str3 ="Geeks"
res = list(chain(str1, str2, str3)) 
print("Before joining :", res) 
ans =''.join(res) 
print("After joining :", ans) 