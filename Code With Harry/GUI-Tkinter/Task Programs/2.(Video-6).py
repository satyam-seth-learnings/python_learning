from tkinter import*
root=Tk()
root.geometry("500x400")
root.minsize(500,400)
root.maxsize(500,400)
root.title("Satyam Seth GUI")
label=Label(text="Ready",bg="red",fg="white",borderwidth=3,font="comicsansms 13 bold",relief=SUNKEN)
label.pack(side=BOTTOM,fill=X)
root.mainloop()