from tkinter import *

def button_press(num):
    pass

def equals():
    pass

def clear():
    pass

window = Tk()

window.title("Calculator prog")
window.geometry('500x500')

equation_text = ""
equstion_lable = StringVar()

label  = Label(window, textvariable=equstion_lable, font=("Helvetica"), bg="white", width=24, height=2)
label.pack( )

frame = Frame(window)
frame.pack()

button_1 = Button(frame, text=1, height=4, width=9, font=35, 
                  command=lambda:button_press(1))
button_1.grid(row=0, column=0)

button_1 = Button(frame, text=1, height=4, width=9, font=35, 
                  command=lambda:button_press(1))
button_1.grid(row=0, column=0)

button_1 = Button(frame, text=1, height=4, width=9, font=35, 
                  command=lambda:button_press(1))
button_1.grid(row=0, column=0)

button_1 = Button(frame, text=1, height=4, width=9, font=35, 
                  command=lambda:button_press(1))
button_1.grid(row=0, column=0)



window.mainloop()