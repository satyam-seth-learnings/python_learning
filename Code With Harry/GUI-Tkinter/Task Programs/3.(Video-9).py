from tkinter import*
root = Tk()
root.geometry("246x38")
root.minsize(246,38)
root.maxsize(246,38)

# function1
def fun1():
    print("Satyam")
# frame1
frame1 = Frame (root , bg = "grey" , borderwidth = 4 , relief = SOLID )
frame1.pack( side = LEFT , anchor = "nw" )
# button1
bt1 = Button ( frame1 , fg = "red" , text = "Satyam" , command = fun1 )
bt1.pack(side=LEFT,padx=2,pady=2)

# function2
def fun2():
    print("Harshit")
# frame2
frame2=Frame(root,bg="grey",borderwidth=4,relief=SOLID)
frame2.pack(side=LEFT,anchor="nw")
# button2
bt2=Button(frame2,fg="red",text="Harshit",command=fun2)
bt2.pack(side=LEFT,padx=2,pady=2)

# function3
def fun3():
    print("Ankit")
# frame3
frame3=Frame(root,bg="grey",borderwidth=4,relief=SOLID)
frame3.pack(side=LEFT,anchor="nw")
# button3
bt3=Button(frame3,fg="red",text="Ankit",command=fun3)
bt3.pack(side=LEFT,padx=2,pady=2)

# function4
def fun4():
    print("Abhishek")
# frame4
frame4=Frame(root,bg="grey",borderwidth=4,relief=SOLID)
frame4.pack(side=LEFT,anchor="nw")
# button4
bt4=Button(frame4,fg="red",text="Abhishek",command=fun4)
bt4.pack(side=LEFT,padx=2,pady=2)

root.mainloop()