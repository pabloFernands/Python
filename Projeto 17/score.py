from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.scoreboard_update()

    def scoreboard_update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def scoreboard_point_add(self, player):
        if player == "l":
            self.l_score += 1
            self.scoreboard_update()
        elif player == "r":
            self.r_score += 1
            self.scoreboard_update()

