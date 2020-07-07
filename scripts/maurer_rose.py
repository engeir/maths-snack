import math, turtle

n = int(input('Give "n"\t'))  # 5
d = int(input('Give "d"\t'))  # 97
c = 0  # int(input('Give "c"\t'))

screen = turtle.Screen()
screen.setup(width=800, height=800, startx=0, starty=0)
screen.bgcolor('black')
pen = turtle.Turtle()
pen.speed(20)

pen.color('blue')
pen.pensize(0.5)
for theta in range(361):
    k = theta * d * math.pi / 180
    r = 300 * math.sin(n * k) + c
    x = r * math.cos(k)
    y = r * math.sin(k)
    pen.goto(x, y)

pen.color('red')
pen.pensize(4)
for theta in range(361):
    k = theta * math.pi / 180
    r = 300 * math.sin(n * k) + c
    x = r * math.cos(k)
    y = r * math.sin(k)
    pen.goto(x, y)
