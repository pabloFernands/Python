from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Jogo da Cobra - Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_points()

    if (snake.snake_head.xcor() > 295 or snake.snake_head.xcor() < -295 or snake.snake_head.ycor() > 295 or snake.
            snake_head.ycor() < -295):
        game_on = False
        scoreboard.game_over()

    for body in snake.snake_body[1:]:
        if snake.snake_head.distance(body) < 5:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
