from turtle import Screen
from peddles import Paddles
from balls import Ball
from scoreboard import Score

import time

screen = Screen()

screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

ball = Ball()
score = Score()


r_paddle = Paddles((370, 0))
l_paddle = Paddles((-370, 0))

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
# screen.onkey(paddles.left, "Left")
# screen.onkey(paddles.right, "Right")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.xcor() > 380:
        score.l_point()
        ball.reset_position()

    if ball.xcor() < -380:
        score.r_point()
        ball.reset_position()

screen.exitonclick()
