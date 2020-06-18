from tkinter import *
from random import randrange as rnd, choice
import time

root = Tk()
root.geometry('800x600')
root.title("Catch the ball")
canvas = Canvas(root, bg="White")
canvas.pack(fill=BOTH,expand=1)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'magenta']
def new_ball():
    """
    Creates a ball with random size, color at random coordinatws every 1000ms
    """
    canvas.delete(ALL)
    global ball_x_cord, ball_y_cord, ball_radius
    ball_x_cord = rnd(100, 700)
    ball_y_cord = rnd(100, 500)
    ball_radius = rnd(30, 50)
    canvas.create_oval(ball_x_cord - ball_radius, ball_y_cord - ball_radius,
                       ball_x_cord + ball_radius, ball_y_cord + ball_radius, fill=choice(colors), width=0)
    root.after(1000, new_ball)

def click_event(event):
    """
    Check, if a click was made in the ball, in this case sends +1 to counter, after, ball is deleted.
    If  click was not in the ball - nothing.
    """
    length_between_p = ((ball_x_cord - event.x) ** 2 + (ball_y_cord - event.y) ** 2) ** 0.5
    if length_between_p <= ball_radius:
        print("попал")
    else:
        print("не попал")




canvas.bind('<Button-1>', click_event)
new_ball()
mainloop()