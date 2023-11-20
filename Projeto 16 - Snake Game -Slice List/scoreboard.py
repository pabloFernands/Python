from turtle import Turtle

ALING = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = Turtle()
        self.score.color("white")
        self.score_count = 0
        with open("data.txt") as data:
            self.score_high = int(data.read())
        self.score.pu()
        self.score.goto(x=0, y=270)
        self.score.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.score.clear()
        self.score.write(arg=f"Your score is: {self.score_count} High score: {self.score_high}", align=ALING, font=FONT)

    def score_points(self):
        self.score.clear()
        self.score_count += 1
        self.update_scoreboard()

    def reset(self):
        if self.score_count > self.score_high:
            self.score_high = self.score_count
            with open("data.txt", mode="w") as data:
                data.write(str(self.score_high))
        self.score_count = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.score.goto(0, 0)
    #     self.score.write(arg="GAME OVER", align=ALING, font=FONT)
