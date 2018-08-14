from turtle import *
import random
# from ex5_draw_star import draw_star

speed(-1)
shape('turtle')
color('green')

def draw_star(x, y, length ):
    penup()
    goto(x, y)
    pendown()

    for i in range(5):
        forward(length)
        right(144)
    

for i in range(100):
    x = random.randint(-300,300)
    y = random.randint(-300,300)

    length = random.randint(3,10)

    draw_star(x, y, length)

mainloop()

