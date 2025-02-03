#widgets are gui elements: button, labels
#windows serve as container to store this widgets

from tkinter import *

root=Tk() #object/instance of a window

root.title("GUI window")

root.geometry("500x500")

icon=PhotoImage(file="C:/Users/Dikshita Kalitkar/OneDrive/Pictures/bts_logo.png")
root.iconphoto(True,icon)

root.config(background="grey")

root.mainloop() #place window on computer screen
