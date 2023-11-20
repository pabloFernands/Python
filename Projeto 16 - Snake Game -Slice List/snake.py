from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_body = []
        self.snake_x = 0
        self.snake_y = 0
        self.create_snake()
        self.snake_head = self.snake_body[0]

    def create_snake(self):
        for x in range(0, 3):
            snake = Turtle(shape="square")
            snake.color("white")
            snake.pu()
            self.snake_body.append(snake)
            snake.goto(x=self.snake_x, y=self.snake_y)
            self.snake_x += -20

    def extend(self):
        last_position = self.snake_body[-1].position()
        snake = Turtle(shape="square")
        snake.hideturtle()
        snake.color("white")
        snake.pu()
        snake.showturtle()
        snake.goto(last_position)
        self.snake_body.append(snake)

    def snake_reset(self):
        for body in self.snake_body:
            body.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.snake_head = self.snake_body[0]


    def move(self):
        for seg_number in range(len(self.snake_body) - 1, 0, -1):
            snake_segment_x = self.snake_body[seg_number - 1].xcor()
            snake_segment_y = self.snake_body[seg_number - 1].ycor()
            self.snake_body[seg_number].goto(snake_segment_x, snake_segment_y)
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
