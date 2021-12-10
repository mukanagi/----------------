from tkinter import *

def submit():
    print("The current temperature is "+str(scale.get())+' degrees C.')

window = Tk()

hot_img = PhotoImage(file="flame.png")
hot_label = Label(image=hot_img)
hot_label.pack()


scale = Scale(window, 
            from_=100, to=-100,
            length=600, font=("Consolas", 25, "bold"),
            fg="##FF7158", bg="#282A36",
            tickinterval = 10, # adds interval set to 10
            showvalue = 0, # hide current value
            resolution = 5, # increment of a slider
            troughcolor = "#72789A"
            )
scale.set(0)
scale.pack()

snow_img = PhotoImage(file="snowflake.png")
snow_label = Label(image=snow_img)
snow_label.pack()

button = Button(window, text="submit", command=submit,)
button.pack()

window.mainloop()