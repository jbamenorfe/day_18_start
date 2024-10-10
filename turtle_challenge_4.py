from turtle import Turtle, Screen
import random

colors = ["red", "orange", "green", "brown", "blue", "violet"]
directions = [0, 90, 180, 270]

tom = Turtle()
tom.pensize(10)
tom.speed(3)
screen = Screen()

height = screen.window_height()

for steps in range(height):
    random_color = random.choice(colors)
    random_direction = random.choice(directions)

    tom.color(random_color)
    tom.left(random_direction)
    tom.forward(20)
    
screen.exitonclick()
