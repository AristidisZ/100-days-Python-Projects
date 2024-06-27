import turtle
from turtle import Turtle, Screen
import random

bet_on = False

screen = Screen()

screen.setup(width=500, height=400)

colors = ["orange", "green", "purple", "black", "blue", "yellow"]
shapes_list = ["turtle", "classic", "square", "arrow", "circle", "triangle"]

user_bet = screen.textinput("NIM", "Whose gonna win: " + ",".join(colors))

while not user_bet:
    user_bet = screen.textinput("NIM", "Whose gonna win: " + ",".join(colors))

y = 150

all_turtles = []

for i in range(6):
    # shape = shapes_list[i]
    # print(shape)
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-200, y=y)
    y -= 50

    new_turtle.color(colors[i])
    all_turtles.append(new_turtle)

if user_bet:
    bet_on = True

while bet_on:
    for turtle in all_turtles:
        print(turtle.color())
        if turtle.xcor() > 230:
            print(f"Winner is :{turtle.pencolor()}")
            bet_on = False
            if turtle.pencolor() == user_bet:
                print("You won the bet")
            else:
                print("you lost the bet")

        distance = random.randint(0, 10)
        if turtle.color()[1] == "orange":
            turtle.forward(10)
        turtle.forward(distance)

screen.exitonclick()
