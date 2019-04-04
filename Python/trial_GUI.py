# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 16:35:18 2018

@author: USER
"""

"""
tkinter usage and window specs
"""
from functools import partial
from tkinter import Tk,Frame,Button,messagebox,LEFT,RIGHT,Label,Y,X
window = Tk()
frame = Frame(window)
window.geometry('480x600')
# title
window.title("My computer thing")

#photo image
#photo1 = PhotoImage(file="logo.gif")
#Label(frame).grid(row=0,column=0,sticky =E)

# label
def func(x=100):
    sting = "a Tk MessageBox " + str(x)
    messagebox.showinfo("Title", sting)

# miscellaneous
func_arg = partial(func, 100)
button1 = Button(frame, padx = 10, pady = 10, text = 'Deposit', command = func_arg,fill=X)
button2 = Button(frame, padx = 10, pady = 10, text = 'Withdraw', command = func_arg,fill=X)

label = Label(window, text = "this is text", fg = 'black' , bg = 'red')
label.pack(side = LEFT, fill = Y)

button1.pack(side = RIGHT)
button2.pack(side = LEFT)

frame.pack()

# text entry box

# submit button

# another label

# text box

# the dictionary

### the main loop (Tk.mainloop())

window.mainloop()