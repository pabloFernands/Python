from turtle import Turtle

ALING = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = Turtle()
        self.score.color("white")
        self.score_count = 0
        self.score.pu()
        self.score.goto(x=0, y=270)
        self.score.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.score.write(arg=f"Your score is: {self.score_count}", align=ALING, font=FONT)

    def score_points(self):
        self.score.clear()
        self.score_count += 1
        self.update_scoreboard()

    def game_over(self):
        self.score.goto(0, 0)
        self.score.write(arg="GAME OVER", align=ALING, font=FONT)
