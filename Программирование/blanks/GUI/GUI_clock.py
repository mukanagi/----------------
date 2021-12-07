from tkinter import *
from time import *

def update():
    day_string = strftime("%A")
    day_label.config(text=day_string)
    
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    date_string = strftime("%d:%m:%y")
    date_label.config(text=date_string)

    window.after(1000, update)

window = Tk()

window.config(bg='#000')

day_label = Label(window, font=('Ink Free', 25), fg='#009900', bg='#000')
day_label.pack()

time_label = Label(window, font=('Arial', 50), fg='#009900', bg='#000')
time_label.pack()

date_label = Label(window, font=('Helvetica', 20), fg='#009900', bg='#000')
date_label.pack()

update()

window.mainloop()