from tkinter import *
from tkinter import messagebox

def click():
    # messagebox.showinfo(title="Additional info", message="You are a person")
    # messagebox.showwarning(title="Warning", message="Be careful")
    # messagebox.showerror(title="Error", message="Error 404")
    # if messagebox.askokcancel(title="ask ok  cancel", message="DO ya wanna do a thing!&? "):
    #     print("U did a thing! ")
    # else:
    #     print("You did not do a thing! ")

    if messagebox.askretrycancel(title="ask ok  cancel", message="DO ya wanna retry a thing!&? "):
        print("U retry a thing! ")
    else:
        print("You did not retry a thing! ")

window = Tk()

button = Button(window, text="click on me", command=click)
button.pack()

window.mainloop()