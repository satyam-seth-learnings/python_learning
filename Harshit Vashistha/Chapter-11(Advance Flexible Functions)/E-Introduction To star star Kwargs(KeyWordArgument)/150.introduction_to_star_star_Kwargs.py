# introduction to **Kwargs (keyWordArgument)
# **Kwargs (double star operator)
# Kwargs as a parameter
def func(**Kwargs):
    print(type(Kwargs))
    print(Kwargs)
    for k,v in Kwargs.items():
        print(f"{k}:{v}")
func(first_name="Satyam",last_name="Seth")
def func1(name,**Kwargs):
    print(Kwargs)
    print(name)
    for k,v in Kwargs.items():
        print(f"{k}:{v}")
func1("Abhi",first_name="Satyam",last_name="Seth")
# dictionary unpacking
d={'name':'Satyanm','age':20}
func(**d)