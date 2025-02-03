from tkinter import *

def fun():
    print(x.get())
root=Tk()
photo=PhotoImage(file="C:/Users/Dikshita Kalitkar/OneDrive/Pictures/bts_logo.png")
x=IntVar()#StringVar
n=Checkbutton(root,text="Option 1",
              variable=x,
              onvalue=1,
              offvalue=0,
              font=('Arial',10,'italic'),
              fg='black',bg='grey',
              activeforeground='black',activebackground='grey',
              image=photo,
              padx=10,pady=10,
              compound=RIGHT,
              
              command=fun)
n.pack()
root.mainloop()
