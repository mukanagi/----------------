from tkinter import *
from tkinter import colorchooser

def click():
    # color = colorchooser.askcolor()
    # color_hex = color[1]
    # window.config(bg=color_hex)
    
    # the same function but less lines of code
    window.config(bg=colorchooser.askcolor()[1])


window = Tk()
window.geometry("420x420")
button = Button(text="click me", command=click)
button.pack()
window.mainloop()
