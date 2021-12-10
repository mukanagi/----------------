from tkinter import *
import time

WIDTH = 500
HEIGHT = 500

x_velocity = 3
y_velocity = 2

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

photo_img = PhotoImage(file='piton.png')
my_img = canvas.create_image(0, 0, image=photo_img, anchor=NW)

img_width = photo_img.width()
img_height = photo_img.height()

while True:
    coordinates = canvas.coords(my_img)
    print(coordinates)
    if(coordinates[0]>=(WIDTH - img_width) or coordinates[0]<0):
        x_velocity = -x_velocity

    if(coordinates[1]>=(HEIGHT - img_height) or coordinates[1]<0):
        y_velocity = -y_velocity

    canvas.move(my_img, x_velocity, y_velocity)
    window.update()
    time.sleep(0.01)

window.mainloop()