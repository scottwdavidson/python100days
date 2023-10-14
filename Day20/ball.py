from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize()
        self.penup()
        self.goto(0, 0)
        self.x_direction = 1
        self.y_direction = -1
        self.speed = 16

    def move(self):

        # "move" ball by adding direction to current ball position
        new_x_coordinate = self.xcor() + self.x_direction * self.speed
        new_y_coordinate = self.ycor() + self.y_direction * self.speed
        self.goto(new_x_coordinate, new_y_coordinate)

    def bounce_y_direction(self):
        self.y_direction *= -1

    def bounce_x_direction(self):
        self.x_direction *= -1
