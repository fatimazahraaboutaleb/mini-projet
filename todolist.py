from tkinter import *
import tkinter as tk
import os
root = Tk()
root.title("To-Do List App")
root.configure(bg="black")
root.geometry("450x500")
root.resizable(False,False)

icon_path=os.path.abspath("C:\\Users\\hp\\Desktop\\dev\\mini projet1\\mini-projet\\icon.png")
icon= tk.PhotoImage(file=icon_path)
root.iconphoto(False, icon)

label=Label(root,text=0, width=10, bg="white", fg="magenta", font=("Helvetica",13))
label.pack(pady=10)

listbox = Listbox(root, width=30, height=8, selectbackground="magenta" ,selectforeground="black",bg="pink" ,fg="purple",font=("Helvetica", 14))
listbox.pack(pady=10)

entry_label=Label(root,text="Enter The Task:", width=12, bg="black", fg="white",font=("Helvetica",10))
entry_label.pack()

new_entry = Entry(root, width=50,  fg="blue")
new_entry.pack(pady=10)

nbr=0
def add():
    global nbr
    task = new_entry.get()
    if task:
        listbox.insert(END, task)
        new_entry.delete(0, END)
    nbr+=1
    label.config(text=nbr)

def delete():
    global nbr
    selected= listbox.curselection()
    listbox.delete(selected)
    nbr-=1
    label.config(text=nbr)

def clear():
    global nbr
    listbox.delete(0,END)
    nbr=0
    label.config(text=nbr)

def pink():
    listbox.config(selectbackground="magenta" ,selectforeground="black",bg="pink" ,fg="purple")
    label.config(fg="magenta")

def green():
    listbox.config(selectbackground="darkgreen" ,selectforeground="black",bg="lightgreen" ,fg="blue")
    label.config(fg="darkgreen")

def yellow():
    listbox.config(selectbackground="gold" ,selectforeground="black",bg="yellow" ,fg="red")
    label.config(fg="orange")

add_btn = Button(root, text="Add Task", width=20, command=add)
add_btn.pack(pady=5)

delete_btn = Button(root, text="Delete Task", width=20, command=delete)
delete_btn.pack(pady=5)

clear_btn=Button(root, text="Clear all", width=20, command=clear)
clear_btn.pack(pady=5)

colors=Label(root,text="Choose A Color:",bg="black",fg="white",font=("Helvetica",10))
colors.pack(pady=5)

Button(root, text="PINK",width=17,command=pink, fg="magenta").pack(side=LEFT,padx=10)
Button(root, text="GREEN",width=17,command=green, fg="green").pack(side=LEFT,padx=10)
Button(root, text="YELLOW",width=17,command=yellow, fg="orange").pack(side=LEFT,padx=10)

root.mainloop()
