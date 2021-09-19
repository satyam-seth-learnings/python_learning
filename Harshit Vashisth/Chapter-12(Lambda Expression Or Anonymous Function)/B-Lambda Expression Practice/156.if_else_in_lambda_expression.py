# Lambda Expression Practice-3
def func(s):
    if len(s)>5:
        return True
    return False
print(func("Satyam"))
func2=lambda s:True if len(s)>5 else False
print(func2("abc"))
func3=lambda s:len(s)>5
print(func3("wxyz"))