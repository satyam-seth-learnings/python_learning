from tkinter import*
root=Tk()
root.geometry("300x400")
# funtion
def getvals():
    print(f"Name:{namevalue.get()}")
    print(f"Mobile No.:{mobilevalue.get()}")
# Label
name=Label(root,text="Name:").grid(row=0)
mobile=Label(root,text="Mobile No:").grid(row=1)
# Variable
namevalue=StringVar()
mobilevalue=StringVar()
# Entry
nameentry=Entry(root,textvariable=namevalue).grid(row=0,column=1)
mobileentry=Entry(root,textvariable=mobilevalue).grid(row=1,column=1)
# Button
Button(text="Submit", command=getvals).grid()
root.mainloop()