from tkinter import *

root = Tk()
root.title("Simple Calculator")

def button_click(number):
    e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)
    e.insert(0,'+')

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)
    e.insert(0,'-')

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)
    e.insert(0,'x')

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)
    e.insert(0,'-')

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    e.insert(0,'=')
    e.delete(0, END)
    
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    elif math == "subtraction":
        e.insert(0, f_num - int(second_number))
    elif math == "multiplication":
        e.insert(0, f_num * int(second_number))
    elif math == "division":
        e.insert(0, f_num / int(second_number))

n1 = IntVar()
n2 = IntVar()
s = StringVar()
f = Frame(root, height=100, width=100,bg='black')
f.pack()
e = Entry(f,bg='black',fg='green')
e.grid(row=0, columnspan=4)

b1 = Button(f, text='1', bg='grey',fg='green',command=lambda: button_click(1))
b1.grid(row=1, column=0)
b2 = Button(f, text='2', bg='grey',fg='green', command=lambda: button_click(2))
b2.grid(row=1, column=1)
b3 = Button(f, text='3', bg='grey',fg='green', command=lambda: button_click(3))
b3.grid(row=1, column=2)
b4 = Button(f, text='+',  bg='grey',fg='green',command=button_add)
b4.grid(row=1, column=3)

b5 = Button(f, text='4',bg='grey',fg='green', command=lambda: button_click(4))
b5.grid(row=2, column=0)
b6 = Button(f, text='5', bg='grey',fg='green',command=lambda: button_click(5))
b6.grid(row=2, column=1)
b7 = Button(f, text='6', bg='grey',fg='green',command=lambda: button_click(6))
b7.grid(row=2, column=2)
b8 = Button(f, text='-', bg='grey',fg='green',command=button_subtract)
b8.grid(row=2, column=3)

b9 = Button(f, text='7',bg='grey',fg='green', command=lambda: button_click(7))
b9.grid(row=3, column=0)
b10 = Button(f, text='8', bg='grey',fg='green',command=lambda: button_click(8))
b10.grid(row=3, column=1)
b11 = Button(f, text='9', bg='grey',fg='green',command=lambda: button_click(9))
b11.grid(row=3, column=2)
b12 = Button(f, text='x', bg='grey',fg='green',command=button_multiply)
b12.grid(row=3, column=3)

b13 = Button(f, text='%',bg='grey',fg='green', command=button_divide)
b13.grid(row=4, column=0)
b14 = Button(f, text='=', bg='grey',fg='green',command=button_equal)
b14.grid(row=4, column=1)
b15 = Button(f, text='C', bg='grey',fg='green',command=button_clear)
b15.grid(row=4, column=2)
b16 = Button(f, text='OFF',bg='grey',fg='green', command=root.quit)
b16.grid(row=4, column=3)

root.mainloop()
