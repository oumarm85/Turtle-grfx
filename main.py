import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

tim = Turtle()
tim.shape("turtle")
tim.color("green")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_color = (r, g, b)
    return my_color

# colours = ["red", "orange", "yellow", "green", "blue", "purple", "black"]

# draw a square
# for _ in range(4):
#     tim.forward(100)
#     tim.rt(90)

# draw a dash line
# for _ in range(15):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)

#draw a different shares in muliple colours
# def create_shape(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.rt(angle)
#
# for sides in range(3, 11):
#     tim.pencolor(random.choice(colours))
#     create_shape(sides)


tim.speed(0)

# random walk
# angles = [0, 90, 180, 270, 360]
# for _ in range(500):
#     tim.pencolor(random_color())
#     tim.forward(40)
#     tim.rt(random.choice(angles))

def draw_spirograpgh(gap):
    for _ in range(int(360 / gap)):
        tim.pencolor(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap)

draw_spirograpgh(2)






screen = Screen()
screen.exitonclick()