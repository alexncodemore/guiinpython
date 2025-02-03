from tkinter import *
from tkinter import messagebox

def fun():
    #messagebox.showinfo(title="message info box",message="Hello world!")
    #messagebox.showwarning(title="Warning",message="Warning message box")
    #messagebox.showerror(title="Error",message="Error message box")
    #messagebox.askokcancel(title="ok/cancel",message="give ans")#True False
    #messagebox.askretrycancel(title="retry/cancel",message="ans..")#True False
    #messagebox.askyesno(title="yes/no",message="ans..")#True False
    #messagebox.askquestion(title"yes /no")#yes no
    messagebox.askyesnocancel(title="yes no cancel",message="ans.",icon="info")#warnning,error,info
root=Tk()

b=Button(root,text="Click Me!",command=fun)
b.pack()
root.mainloop()
