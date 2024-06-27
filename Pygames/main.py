import turtle as t
from turtle import Screen
import random

turtle = t.Turtle()
t.colormode(255)


def random_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    x = (r, g, b)
    return x


turtle.speed("fastest")
variable = 0
turtle.pensize(3)
size_gap = 10
for _ in range(int(360/size_gap)):
    turtle.color(random_rgb())
    turtle.circle(150)
    turtle.setheading(turtle.heading()+size_gap)


# colors = ["Blue", "Red", "Green", "Yellow", "Purple", "Grey"]
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# for _ in range(200):
#     tim.color(random_rgb())
#     tim.setheading(random.choice(directions))
#     tim.forward(30)
#
# #
screen = Screen()
screen.exitonclick()


#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.color(random.choice(colors))
#         tim.forward(100)
#         tim.right(angle)
#     for _ in range(num_sides):
#         tim.color(random.choice(colors))
#         tim.forward(100)
#         tim.left(angle)
#
#
# for shape in range(3, 11):
#     # tim.color(random.choice(colors))
#     tim.pensize(3)
#     draw_shape(shape)
