from tkinter import*
root=Tk()
# WidthxHeight
root.geometry("644x483")
# width,height
root.minsize(200,100)
# width,height
root.maxsize(800,600)
# lable
satyam=Label(text="Hi Satyam,this is your GUI")
satyam.pack()
root.mainloop()