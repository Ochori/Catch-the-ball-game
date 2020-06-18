from tkinter import *
from random import randrange as rnd, choice
import time

root = Tk()
root.geometry('800x600')
root.title("Catch the ball")
canvas = Canvas(root, bg="White")
canvas.pack()

colors = ['red', 'orange', 'yellow', 'green', 'blue']
def new_ball():
    canvas.delete(ALL)
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    canvas.create_oval(x - r, y - r, x + r, y + r, fill=choice(colors), width=0)
    root.after(1000, new_ball)


new_ball()
mainloop()