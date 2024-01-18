from tkinter import *
root = Tk()
root.title("To-Do List App")
root.configure(bg="black")
root.geometry("450x500")
root.resizable(False,False)
label=Label(root,text=0, width=10, bg="white", fg="magenta", font=10)
label.pack(pady=10)
listbox = Listbox(root, width=30, height=8, selectbackground="magenta" ,selectforeground="black",bg="pink" ,fg="purple",font=("Helvetica", 14))
listbox.pack(pady=10)
entry_label=Label(root,text="Enter The Task:", width=10, bg="black", fg="white")
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
    listbox.config(selectbackground="orange" ,selectforeground="black",bg="yellow" ,fg="red")
    label.config(fg="orange")

add_btn = Button(root, text="Add Task", width=20, command=add)
add_btn.pack(pady=5)

delete_btn = Button(root, text="Delete Task", width=20, command=delete)
delete_btn.pack(pady=5)

clear_btn=Button(root, text="Clear all", width=20, command=clear)
clear_btn.pack(pady=5)
colors=Label(root,text="CHOOSE A COLOR:",bg="black",fg="white")
colors.pack()
Button(root, text="PINK",width=20,command=pink).pack(side=LEFT)
Button(root, text="GREEN",width=20,command=green).pack(side=LEFT)
Button(root, text="yellow",width=20,command=yellow).pack(side=LEFT)

root.mainloop()
