from tkinter import *
import time
from ball import *

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas, 0, 0, 90, 12, 16, 'white')
tennis_ball = Ball(canvas, 1, 1, 50, 20, 24, 'yellow')
basket_ball = Ball(canvas, 3, 3, 75, 12, 18, 'orange')
soccer_ball = Ball(canvas, 4, 4, 110, 5, 14, 'blue')

while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    soccer_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()