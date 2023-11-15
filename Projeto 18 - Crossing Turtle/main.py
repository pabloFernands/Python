import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.car_create()
    car_manager.car_move()

    for car in car_manager.car_list:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

        if player.player_finish():
            player.restart_player()
            car_manager.car_increment_speed()
            scoreboard.scoreboard_update()




screen.exitonclick()