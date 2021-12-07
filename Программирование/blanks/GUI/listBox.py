from tkinter import *
from tkinter import font

def add():
    list_box.insert(list_box.size(), entry_box.get())
    list_box.config(height=list_box.size())
    
def delete():
    for index in reversed(list_box.curselection()):
        list_box.delete(index)
        
    list_box.config(height=list_box.size())

def submit():
    food = []

    for index in list_box.curselection():
        food.insert(index, list_box.get(index))

    print("You ordered ", )
    for index in food: print(index)

window = Tk()

list_box = Listbox(window, font=("Open Sans", 30, "bold"), bg="#FFE856",
                   width=18, selectmode=MULTIPLE
                   )
list_box.pack()

list_box.insert(1, "Pizza")
list_box.insert(2, "Spaghetti")
list_box.insert(3, "Mashpatato")
list_box.insert(4, "Shashlik")
list_box.insert(5, "Grilled Dorado")

list_box.config(height=list_box.size())

entry_box = Entry(window)
entry_box.pack()

add_button = Button(window, text="Add to menu", font=("Open Sans", 20), command=add)
add_button.pack()

delete_button = Button(window, text="Delete from menu", font=("Open Sans", 20), command=delete)
delete_button.pack()

submit_button = Button(window, text="Submit Your order", font=("Open Sans", 20), command=submit)
submit_button.pack()

print("hello")

window.mainloop()