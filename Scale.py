from tkinter import *

def fun():
    print(s.get())
photo=PhotoImage(file="C:/Users/Dikshita Kalitkar/OneDrive/Pictures/bts_logo.png")
root=Tk()

s=Scale(root,from_=100,to=0,
        orient=VERTICAL,
        length=200,
        tickinterval=10,
        font=("Arial",5),
        showvalue= 0,
        resolution=0,
        fg="green",
        bg="grey",
        troughcolor="pink")
s.pack(side=RIGHT)
s.set=(10)
b=Button(root,text="Submit",command=fun)
b.pack(side=BOTTOM)


root.mainloop()
