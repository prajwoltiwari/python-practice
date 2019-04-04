from tkinter import *
from tkinter import messagebox
from functools import partial

root = Tk()
root.geometry('1240x720')

topframe = Frame(root)
topframe.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

def window_popup(x=100):
    string = "This is the message popup.\n" + str(x)
    messagebox.showinfo("Title", string )

partial_func = partial(window_popup,100)
button1 = Button(topframe, padx=10, pady=20, text="Button 1", fg="red", bg="cyan", command = partial_func)
button2 = Button(topframe, text="Button 2", fg="blue")
button3 = Button(topframe, text="Button 3", fg="green")
button4 = Button(bottomframe, text="Button 4", fg="purple")

button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = LEFT)
button4.pack(side = RIGHT)

thelabel = Label(root, text="This is a python testing GUI.", fg="pink", bg="blue")
thelabel.pack(side = LEFT, fill=Y)

root.mainloop()