def function1(a,b):
	print("Hello you are in function 1", a+b)
def function2(a,b):
	"""This will the function which will calculate of two numbers
	this function dosent work for three numbers"""
	average =(a+b)/2
	#	print(average)
	return average
	
#	v=function2(5 , 7)
#	print(v)
print(function2.__doc__)
	