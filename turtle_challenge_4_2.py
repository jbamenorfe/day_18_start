from turtle import Screen
import turtle as t
import random


#colors = ["red", "orange", "green", "brown", "blue", "violet"]
directions = [0, 90, 180, 270]

tom = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)


tom.pensize(7)
tom.speed(3)
screen = Screen()

for steps in range(200):
    random_direction = random.choice(directions)

    tom.color(random_color())
    tom.left(random_direction)
    tom.forward(20)
    
screen.exitonclick()
