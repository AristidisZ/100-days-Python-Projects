from turtle import Screen


from scoreboard import Score
from Snake import Snake
import time
from food import Food

screen = Screen()
screen.bgcolor("black")
screen.setup(width=500, height=500)
screen.tracer(0)

score = Score()

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    if snake.head.xcor() > 240 or snake.head.xcor() < -240 or snake.head.ycor() > 240 or snake.head.ycor() < -240:
        score.reset_score()
        snake.reset_snake()

    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_score()
            snake.reset_snake()


    # for segment in snake.segment:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         score.game_over()
    #         game_is_on = False

screen.exitonclick()
