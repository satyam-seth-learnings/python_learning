# function with all paremeters
# PADK=(parameter,*args,defalut,**Kwargs)
def func(name,*args,last_name='unknown',**Kwargs):
    print(name)
    print(args)
    print(last_name)
    print(Kwargs)
func("Satyam",1,2,3,a=1,b=2)