from turtle import Screen
from snake import Snake
from breadcrumb import Breadcrumb
import time


class Controller:
    screen = Screen()
    current_direction = "r"
    score = 0

    def __init__(self, screen_height, screen_width, snake, breadcrumb):

        # store screen dimensions, snake and breadcrumb
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.screen_boundary = [
            (-1 * int(screen_width / 2) + 10, -1 * int(screen_height / 2) + 10),
            (+1 * int(screen_width / 2) - 10, +1 * int(screen_height / 2) - 10)]
        self.snake = snake
        self.breadcrumb = breadcrumb

        # set up the screen
        self.screen.setup(width=self.screen_width, height=self.screen_height)
        self.screen.bgcolor("black")
        self.screen.tracer(0)

        # configure keyboard monitoring
        self.screen.listen()
        self.screen.onkey(lambda: self.set_snake_direction("r"), "Right")
        self.screen.onkey(lambda: self.set_snake_direction("l"), "Left")
        self.screen.onkey(lambda: self.set_snake_direction("u"), "Up")
        self.screen.onkey(lambda: self.set_snake_direction("d"), "Down")

        # display the snake and breadcrumb
        self.screen.update()

    def snake_head_is_in_bounds(self, snake_head_position):
        if (snake_head_position[0] < self.screen_boundary[0][0]
                or snake_head_position[0] > self.screen_boundary[1][0]
                or snake_head_position[1] < self.screen_boundary[0][1]
                or snake_head_position[1] > self.screen_boundary[1][1]):
            print(f"Out of bounds: {snake_head_position} , {self.screen_boundary}")
            return False
        else:
            return True

    def move_snake(self):
        self.snake.move_snake(self.current_direction)
        self.screen.update()
        time.sleep(0.05)

        # check for consuming breadcrumb ( BUMP SCORE +1 )
        snake_head_position = self.snake.head_position()
        if self.breadcrumb.landed_on_breadcrumb(snake_head_position[0], snake_head_position[1]):
            self.score += 1
            print(f"SCORE: {self.score}")
            self.breadcrumb.drop_breadcrumb()

        # check for moving out of bounds and return check value
        return self.snake_head_is_in_bounds(snake_head_position)

    def set_snake_direction(self, direction):
        self.current_direction = direction

    def drop_breadcrumb(self):
        self.breadcrumb.drop_breadcrumb()
        self.screen.update()
