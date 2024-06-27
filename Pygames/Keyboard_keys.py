from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
screen.setup(width=500 ,height=500)

def move_forward():
    t.forward(50)


def move_backwards():
    t.backward(50)


def left():
    t.left(10)


def right():
    t.right(10)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=left, key="a")
screen.onkey(fun=right, key="d")
screen.onkey(fun=clear, key="c")

screen.exitonclick()
