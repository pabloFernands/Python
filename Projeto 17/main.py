from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Jogo - Pong")
screen.tracer(0)
#time.sleep(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_paddle_up, "Up")
screen.onkey(r_paddle.move_paddle_down, "Down")

screen.onkey(l_paddle.move_paddle_up, "w")
screen.onkey(l_paddle.move_paddle_down, "s")

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.ball_move()


    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.ball_bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.ball_bounce_x()

    elif ball.xcor() > 390:
        ball.ball_reset()
        ball.ball_bounce_x()
        scoreboard.scoreboard_point_add("l")

    elif ball.xcor() < -390:
        ball.ball_reset()
        ball.ball_bounce_x()
        scoreboard.scoreboard_point_add("r")




screen.exitonclick()
