# This challenge shows how to draw a spirograph with the turtle graphics.
import turtle as t
import random

def random_color():
    """Returns a random rgb colors"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

timmy = t.Turtle()
t.colormode(255)

def draw_spirograph(size_of_gap):
    number_of_circles = int(360/size_of_gap)
    for gap in range(number_of_circles):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.left(size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()