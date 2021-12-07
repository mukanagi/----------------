from tkinter import *
from tkinter import font

def submit():
    input = text.get("1.0", END)
    print(input)

window = Tk()

text = Text(window, bg='#F3E9B5', font=('Ink Free', 25, 'bold'),
            height=8, width=20,
            padx=20, pady=20,
            fg='#282A36')
text.pack()


button = Button(window, text="submit", command=submit)
button.pack()

window.mainloop()