i=0
def myfun():
    global i
    i+=1
    print("Satyam Seth",i)
    myfun()
myfun()