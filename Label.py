#Label is an area widget that holds text or image within window
from tkinter import *

root=Tk()
#text
'''
label=Label(root,text="Hello World",
            font=("Arial",20,"italic"),
            fg="white",
            bg="black",
            relief=RAISED,
            bd=5,
            padx=20,
            pady=20)

#label.pack()
label.place(x=250,y=100)
'''
#photo
'''
photo=PhotoImage(file='C:/Users/Dikshita Kalitkar/OneDrive/Pictures/bts_logo.png')

l=Label(root,image=photo)
l.pack()
'''
#BOTH
photo=PhotoImage(file='C:/Users/Dikshita Kalitkar/OneDrive/Pictures/bts_logo.png')
l=Label(root,text="BTS ARMY",image=photo,compound='bottom',relief=SUNKEN)
l.pack()
root.mainloop()

#padding means distance between content and boarder
