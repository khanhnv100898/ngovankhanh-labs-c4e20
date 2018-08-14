from turtle import *

def draw_square(length, square_color):
    color(square_color)
    for i in range(4):
        forward(length)
        left(90)