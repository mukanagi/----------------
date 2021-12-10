from tkinter import *
from tkinter import font

food = ["pizza", "hamburger", "hotdog"]

def order():
    if (x.get()==0):
        print("You ordered pizza")
    elif(x.get()==1):
        print("You ordered hamburger")
    elif(x.get()==2):
        print("You ordered hotdog")
    

window = Tk()

pizza_img = PhotoImage(file="pizza.png")
hamburger_img = PhotoImage(file="hamburger.png")
hotdog_img = PhotoImage(file="hotdog.png")
food_images = [pizza_img, hamburger_img, hotdog_img]


x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              bg="#fff",
                              text=food[index], # adds text to radiobutton
                              variable=x, # groups radiobuttons together if they share the sane variable
                              value=index, # assigns each radiobutton different value
                              padx=25,font=("Impact", 34),
                              image=food_images[index], # set image to radiobutton
                              compound='left', # adds img and text(leftside)
                              indicatoron=0, width=380, anchor=W, # eliminate circle indicators
                              command=order # set command of radiobutton to function
                              )
    radiobutton.pack(anchor=W) # выравнивает по левому краю

window.mainloop()