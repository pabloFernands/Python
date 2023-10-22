from turtle import Turtle, Screen

tartaruga = Turtle()
screen = Screen()


def move_foward():
    tartaruga.forward(10)


def move_backward():
    tartaruga.backward(10)


def move_left():
    tartaruga.left(10)


def move_right():
    tartaruga.right(10)


def clear():
    # tartaruga.clear()
    tartaruga.reset()


def move():
    screen.onkey(move_foward, "w")
    screen.onkey(move_backward, "s")
    screen.onkey(move_left, "a")
    screen.onkey(move_right, "d")
    screen.onkey(clear, "c")


move()
screen.listen()
screen.exitonclick()
