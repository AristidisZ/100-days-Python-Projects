from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.hideturtle()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(-200, 260)
        self.update_level()

    def update_level(self):
        self.write(f"Level = {self.level}", False, align="center", font=FONT)

    def game_over(self):
        self.color("black")
        self.goto(0, 0)
        self.write(f"Game Over", False, "center", FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.update_level()
        self.update_level()
