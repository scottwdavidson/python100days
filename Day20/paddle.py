from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, initial_x_coordinate, initial_y_coordinate, minimum_y_coordinate, maximum_y_coordinate):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(initial_x_coordinate, initial_y_coordinate)
        self.minimum_y_coordinate = minimum_y_coordinate
        self.maximum_y_coordinate = maximum_y_coordinate

    def paddle_up(self):
        print(f"(up) {self.ycor()} , {self.maximum_y_coordinate}")
        if self.ycor() < self.maximum_y_coordinate - 50:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def paddle_down(self):
        print(f"(down) {self.ycor()} , {self.minimum_y_coordinate}")
        if self.ycor() > self.minimum_y_coordinate + 50:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
