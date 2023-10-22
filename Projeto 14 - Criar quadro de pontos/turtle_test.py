import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.shape("turtle")
tim.hideturtle()
tim.speed(0)
tim.color("green")
tim.pensize(2)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    value_color = (r, g, b)
    return value_color



angle = [90, 180, 270, 360]

for x in range(200):
    #tim.right(random.choice(angle))
    tim.circle(120)
    #tim.forward(2)
    tim.right(2)
    tim.pencolor(random_color())

random_color()
screen = t.Screen()
screen.exitonclick()