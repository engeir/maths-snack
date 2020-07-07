import turtle
import random

space = 20
w = 800
h = 800


screen = turtle.Screen()
screen.setup(width=w, height=h, startx=0, starty=0)
screen.bgcolor('black')
pen = turtle.Turtle()
pen.speed(20)

pen.color('white')
pen.pensize(1)
pen.penup()

for y in range(- int(h / 2), int(h / 2), space):
    for x in range(- int(w / 2), int(w / 2), space):
        c = random.uniform(- int(w / 2), int(w / 2) - space)
        c = bool(c < x)
        if not c:
            y0 = y
            y1 = y + space
        elif c:
            y0 = y + space
            y1 = y
        pen.goto(x, y0)
        pen.pendown()
        pen.goto(x + space, y1)
        pen.penup()
