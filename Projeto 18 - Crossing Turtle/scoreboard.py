from turtle import Turtle

FONT = ("Courier", 26, "normal")
SCORE_POSITION = (-270, 250)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.hideturtle()
        self.color("black")
        self.level = 0
        self.scoreboard_update()

    def scoreboard_update(self):
        self.clear()
        self.goto(SCORE_POSITION)
        self.level += 1
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=FONT)