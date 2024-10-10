from turtle import Turtle, Screen

# Create a turtle
tim = Turtle()

# Drawing a dashed line with the turtle tim
for step in range (15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
screen = Screen()
screen.exitonclick()
