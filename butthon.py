#Button
from tkinter import *
def fun():
    print("hello!")
root=Tk()
'''
photo=PhotoImage(file='C:/Users/Dikshita Kalitkar/OneDrive/Pictures/bts_logo.png')
b=Button(root,text="Click me",command=fun,
         font=("Comic Sans",30,"bold"),
         fg="white",
         bg="black",
         activeforeground="white",
         activebackground="black",
         state=ACTIVE,
         image=photo,
         compound='bottom')#state=DISABLED
b.pack()
'''

# Buttun counter
i=0
def fun():
    global i
    i+=1
    print("It's",i)
b=Button(root,text="Click me",command=fun)
b.pack()
root.mainloop()
