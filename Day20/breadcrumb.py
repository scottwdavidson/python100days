from turtle import Turtle
import random


class Breadcrumb:
    """Represents the breadcrumb on the screen which the snake will be navigate to 'cross'.
    A twentieth ( 1/20 ) scale screen dimension is used to ensure that the snake head lands directly
    on top of the breadcrumb to make things easier.
    """
    one_twentieth_screen_dimensions = []
    breadcrumb_position = None

    def __init__(self, screen_height, screen_width):
        self.breadcrumb = Turtle(shape="square")
        self.breadcrumb.color("green")
        self.breadcrumb.shapesize(0.5,0.5)
        self.breadcrumb.penup()

        scaled_screen_height = int(screen_height / 20)
        scaled_screen_width = int(screen_width / 20)
        self.one_twentieth_screen_dimensions = [
            (-1 * int(scaled_screen_height / 2) + 1, -1 * int(scaled_screen_width / 2) + 1),
            (int(scaled_screen_height / 2 - 1), int(scaled_screen_width / 2) - 1)]
        self.drop_breadcrumb()

    def landed_on_breadcrumb(self, x_coordinate, y_coordinate):
        if self.breadcrumb_position[0] == x_coordinate and self.breadcrumb_position[1] == y_coordinate:
            return True
        else:
            return False

    def drop_breadcrumb(self):
        x_coordinate = random.randint(self.one_twentieth_screen_dimensions[0][0],
                                      self.one_twentieth_screen_dimensions[1][0]) * 20
        y_coordinate = random.randint(self.one_twentieth_screen_dimensions[0][1],
                                      self.one_twentieth_screen_dimensions[1][1]) * 20
        self.breadcrumb_position = (x_coordinate, y_coordinate)
        self.breadcrumb.goto(x_coordinate, y_coordinate)
