from turtle import Turtle
import random

class Ball(Turtle):

    angle_ball_start = random.randrange(20, 90, 10)
    angle_ball_bot_r = random.randrange(20, 70, 10)
    angle_ball_top_r = random.randrange(290, 340, 10)

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(1, 1)
        self.color("white")
        self.setposition(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def ball_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def ball_bounce_y(self):
        self.y_move *= -1

    def ball_bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def ball_reset(self):
        self.setposition(0, 0)
        self.ball_speed = 0.1


