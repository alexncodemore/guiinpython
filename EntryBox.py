from tkinter import *
#Entry Box : widget in python that accepts single line of input from user

def submit():
    print(n.get())
    #n.config(state=DISABLED)
    
def delete():
    n.delete(0,END)

def backspace():
    n.delete(len(n.get())-1,END)
root=Tk()


n=Entry(root,font=("Arial",20),fg="black",bg="pink",relief=SUNKEN,bd=5)
n.pack(side=LEFT)
#for pwd 'show="*"'

#n.insert(0,'Type something')#default value

b=Button(root,text="Submit",font=("Arial",20),fg="white",bg="black",relief=SUNKEN,bd=5,command=submit)
b.pack(side=RIGHT)
b2=Button(root,text="Delete",font=("Arial",20),fg="white",bg="black",relief=SUNKEN,bd=5,command=delete)
b2.pack(side=RIGHT)
b3=Button(root,text="backspace",font=("Arial",20),fg="white",bg="black",relief=SUNKEN,bd=5,command=backspace)
b3.pack(side=RIGHT)

root.mainloop()
