from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Advinhe o vencedor ", prompt="Qual tartaruga vai ganhar? vermelho, laranja, verde, azul, amarelo ou roxo?")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-100, -60, -20, 20, 60, 100]
all_turtles = []


for turtle_number in range(0, 6):
    turtle_racer = Turtle(shape="turtle")
    turtle_racer.color(color[turtle_number])
    turtle_racer.pu()
    turtle_racer.goto(x=-235, y=y_position[turtle_number])
    all_turtles.append(turtle_racer)

if user_bet:
    race_on = True

while race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning = turtle.pencolor()
            if winning == user_bet:
                print(f"Você ganhou! A cor {winning} é a vencedora.")
            else:
                print(f"Você perdeu! A cor {winning} é a vencedora.")

        moving = random.randint(0, 10)
        turtle.forward(moving)

screen.listen()
screen.exitonclick()
