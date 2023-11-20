from turtle import Turtle


class Paddle(Turtle):

    MOVE = 20

    """
    Classe criadora da raquete. 
    Apos iniciar a super Classe Turtle não foi preciso criar um objeto da class.
    """

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(1, 5)
        self.pu()
        self.goto(position)
        self.setheading(90)

    def move_paddle_up(self):
        self.forward(self.MOVE)

    def move_paddle_down(self):
        self.backward(self.MOVE)
