# Nested Function
def disp():
    def show():
        print("Show Function")
    print("Disp Function")
    show()
disp()

def disp1(st):
    def show1():
        return "Show Function "
    result=show1()+st+" Disp Function"
    return result
print(disp1("Satyam"))