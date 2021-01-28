# replase() method
# find() method
string="she is beautiful and she is good dancer"
string1="is she is beautiful and she is good dancer"
print(string.replace(" ","_"))
print(string.replace("is","was"))
print(string.replace("is","was",1))
print(string.replace("is","was",2))
print(string.replace("is","was",3))
print(string.find("is"))
print(string1.find("is"))
print(string1.find("is",1))
is_position1=(string.find("is"))
is_position2=(string.find("is",is_position1))
print(is_position2)
is_position2=(string.find("is",is_position1+1))
print(is_position2)