from collections import UserDict 
# Creating a Dictionary where deletion is not allowed 
class MyDict(UserDict): 
	# Function to stop deleltion from dictionary 
	def __del__(self): 
		raise RuntimeError("Deletion not allowed") 
	# Function to stop pop from dictionary 
	def pop(self, s = None): 
		raise RuntimeError("Deletion not allowed") 
	# Function to stop popitem from dictionary 
	def popitem(self, s = None): 
		raise RuntimeError("Deletion not allowed") 
# Driver's code 
d = MyDict({'a':1, 
	'b': 2, 
	'c': 3}) 
print("Original Dictionary") 
print(d) 
d.pop(1)  #   RuntimeError: Deletion not allowed
d.popitem() #   RuntimeError: Deletion not allowed