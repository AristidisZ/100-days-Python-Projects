from turtle import Turtle
import pandas as pd

ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")


class Score(Turtle):
    def __init__(self):
        super(Score, self).__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 225)
        self.update_score()
        self.hideturtle()
        # self.clear()

    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score} High score = {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def game_over(self):
        self.reset_score()
        self.color("white")
        self.goto(0, 0)
        self.write(f"Game Over", False, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
