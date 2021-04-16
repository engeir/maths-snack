import math

import matplotlib.pyplot as plt
import numpy as np

a = int(input('Give "a"\t'))  # 5
b = int(input('Give "b"\t'))  # 97
c = int(input('Give "c"\t'))

# screen = turtle.Screen()
# screen.setup(width=800, height=800, startx=0, starty=0)
# screen.bgcolor('white')
# turtle.ht()
# pen = turtle.Turtle()
# pen.ht()
# pen.speed(100)
# pen.shape('turtle')

# pen.color('black')
# pen.pensize(0.5)
x_l = []
y_l = []
for r in np.linspace(0, 100, 120):
    # pen.penup()
    x_ = []
    y_ = []
    for t in np.linspace(0, 361, 1000):
        t *= math.pi / 180
        k = r * (2 + 0.5 * math.sin(a * t))
        x = k * math.cos(t + math.sin(b * t) / c)
        y = k * math.sin(t + math.sin(b * t) / c)
        x_.append(x)
        y_.append(y)
        # pen.goto(x, y)
        # pen.pendown()
    x_l.append(x_)
    y_l.append(y_)

# ts = turtle.getscreen()
# ts.getcanvas().postscript(file=f'starr_rose-{a}_{b}_{c}.eps')

x_arr = np.array(x_l)
y_arr = np.array(y_l)

plt.figure(figsize=(9.5, 9.5))
plt.plot(x_arr.T, y_arr.T, "k", linewidth=3, alpha=0.4)
plt.axis("off")
plt.tight_layout()
# plt.savefig(f'starr_rose-{a}_{b}_{c}.pdf', format='pdf', bbox_inches='tight')
plt.show()
