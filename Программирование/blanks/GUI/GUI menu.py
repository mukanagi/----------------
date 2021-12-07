from tkinter import *

def open_file():
    pass

def save_file():
    pass

def exit_menu():
    print("Program was closed")


window = Tk()

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File")

file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_menu)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")
edit_menu.add_separator()
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Paste")

selection_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Selection", menu=selection_menu)


window.mainloop()