# python tkinter tutorial
# tee-kinter,tk-inter,kinter
# stater code
# from tkinter import *
# win=Tk()
# import tkinter
# win=tkinter.Tk()
import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os
win=tk.Tk()
win.title('GUI')
# create labels
# widgets -->label,buttons,radio button-tk,ttk
# pack,grid
# ttk.Label(win,text='Enter your name: ').pack()
name_label=ttk.Label(win,text='Enter your name: ')
name_label.grid(row=0,column=0,sticky=tk.W)
email_label=ttk.Label(win,text="Enter your email: ")
email_label.grid(row=1,column=0,sticky=tk.W)
age_label=ttk.Label(win,text="Enter your age: ")
age_label.grid(row=2,column=0)
gender_label=ttk.Label(win,text="Enter your gender: ")
gender_label.grid(row=3,column=0,sticky=tk.W)
# create entry box
name_var=tk.StringVar()
name_entrybox=ttk.Entry(win,width=16,textvariable=name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()
email_var=tk.StringVar()
email_entrybox=ttk.Entry(win,width=16,textvariable=email_var)
email_entrybox.grid(row=1,column=1)
age_var=tk.StringVar()
age_entrybox=ttk.Entry(win,width=16,textvariable=age_var)
age_entrybox.grid(row=2,column=1)
# create combobox
gender_var=tk.StringVar()
gender_combobox=ttk.Combobox(win,width=14,textvariable=gender_var,state='readonly')
gender_combobox['values']=('Male','female','other')
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1)
# create radio button
# student,teacher
usertype=tk.StringVar()
radiobtr1=ttk.Radiobutton(win,text='Student',value='Student',variable=usertype)
radiobtr1.grid(row=4,column=0)
radiobtr2=ttk.Radiobutton(win,text='Teacher',value='Teacher',variable=usertype)
radiobtr2.grid(row=4,column=1)
# create check button
checkbtn_var=tk.IntVar()
chickbtn=ttk.Checkbutton(win,text="Check if you want to subscribe to our newsletter",variable=checkbtn_var)
chickbtn.grid(row=5,columnspan=3)
# write to text file
# def action():
#     user_name=name_var.get()
#     user_email=email_var.get()
#     user_age=age_var.get()
#     print(f"{user_name} is {user_age} years old, {user_email}")
#     user_gender=gender_var.get()
#     user_type=usertype.get()
#     if checkbtn_var.get()==0:
#         subscribed='No'
#     else:
#         subscribed='Yes'
#     print(user_gender,user_type,subscribed)
#     with open('File.txt','a') as f:
#         f.write(f'{user_name},{user_age},{user_email},{user_gender},{user_type},{subscribed}\n')
#     name_entrybox.delete(0,tk.END)
#     age_entrybox.delete(0,tk.END)
#     email_entrybox.delete(0,tk.END)
#     name_label.configure(foreground='Blue')
#     age_label.configure(foreground='#b388ff')
#     submit_button.configure(foreground='Red')
# write to csv file
def action():
    user_name=name_var.get()
    user_email=email_var.get()
    user_age=age_var.get()
    user_type=usertype.get()
    user_gender=gender_var.get()
    if checkbtn_var.get()==0:
        subscribed='No'
    else:
        subscribed='Yes'
    with open('File.csv','a',newline='') as f:
        dict_wirter=DictWriter(f,fieldnames=['User Name','User Email Address','User Age','User Gender','User Type','Subscribed'])
        if os.stat('File.csv').st_size==0:
            dict_wirter.writeheader()
        dict_wirter.writerow({'User Name':user_name,'User Email Address':user_email,'User Age':user_age,'User Gender':user_gender,'User Type':user_type,'Subscribed':subscribed})
    name_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)
    name_label.configure(foreground='Blue')
    age_label.configure(foreground='#b388ff')
    submit_button.configure(foreground='Red')
# create button
submit_button=tk.Button(win,text="Submit",command=action)
submit_button.grid(row=6,column=0)
win.mainloop()