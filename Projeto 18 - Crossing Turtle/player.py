from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 300


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.pu()
        self.setheading(90)
        self.goto(STARTING_POSITION)


    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.backward(MOVE_DISTANCE)

    def restart_player(self):
        self.goto(STARTING_POSITION)

    def player_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False