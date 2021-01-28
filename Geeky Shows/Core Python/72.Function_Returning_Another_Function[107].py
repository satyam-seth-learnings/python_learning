def disp():
    def show():
        return "Show Function"
    print("Disp Function")
    return show
r_sh=disp()
print(r_sh())
print(r_sh)

def display(sh):
    print("Display Function")
    return sh
def shows():
    return "Shows Function"
r_sh1=display(shows)
print(r_sh1())