from turtle import Turtle, Screen
import random

# random colors
colors = ["magenta", "aqua", "yellowgreen", "cyan", "blue", "lime", "red"]

tom = Turtle()

for polygon_side in range (3,11):
    polygon_angle = 360/polygon_side
    polygon_color = random.choices(colors)
    tom.color(polygon_color)
    
    for side in range(polygon_side):
        tom.forward(100)
        tom.right(polygon_angle)

screen = Screen()
screen.exitonclick()