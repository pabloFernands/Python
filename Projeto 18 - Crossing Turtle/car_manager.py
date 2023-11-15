from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
#for road in range(-240, 250, 30):


class CarManager:

    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def car_create(self):
        ran_chance = random.randint(1,5)
        if ran_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(1, 2)
            new_car.pu()
            random_y = random.randint(-250, 250)
            new_car.goto(x=300, y=random_y)
            #self.new_speed = (STARTING_MOVE_DISTANCE + MOVE_INCREMENT)
            self.car_list.append(new_car)

    def car_move(self):
        for car in self.car_list:
            car.backward(self.car_speed)

    def car_increment_speed(self):
        self.car_speed += MOVE_INCREMENT

