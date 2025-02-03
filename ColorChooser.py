from tkinter import *
from tkinter import colorchooser #sub module
def fun():
    color=colorchooser.askcolor()#((r,g,b),hex)
    rgbcolor=color[0]
    hexcolor=color[1]
    #print(rgbcolor,hexcolor)
    #root.config(bg=hexcolor)
    
root=Tk()

b=Button(root,text="Click me!",command=fun)
b.pack()

root.mainloop()
