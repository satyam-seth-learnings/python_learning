from tkinter import*
from PIL import Image, ImageTk
root=Tk()
root.geometry("224x224")
# for jpg images
image=Image.open("4.jpg")
photo=ImageTk.PhotoImage(image)
label=Label(image=photo)
label.pack()
root.mainloop()