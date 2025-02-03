from tkinter import *

def fun():
    #print(l.get(l.curselection()))
    food=[]

    for i in l.curselection():
        #print(l.curselection())
        food.insert(i,l.get(i))
    for i in food:
        print(i)
    
def add():
    l.insert(l.size(),e.get())

def delete():
    #l.delete(l.curselection())
    ##l.config(height=l.size())
    for i in reversed(l.curselection()):
        l.delete(i)
        

root=Tk()

l=Listbox(root,
          bg="pink",
          fg="blue",
          font=("Constantia",12,"italic"),
          height=10,width=30,
          selectmode=MULTIPLE)
l.pack()

l.insert(1,"Python")
l.insert(2,"Java")
l.insert(3,"C++")

#l.config(height=l.size())

e=Entry(root)
e.pack()

b1=Button(root,text="Add",command=add)
b1.pack()

b2=Button(root,text="Delete",command=delete)
b2.pack()

b3=Button(root,text="Submit",command=fun)
b3.pack()


root.mainloop()
