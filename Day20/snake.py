from turtle import Turtle


class Snake:
    NUMBER_OF_SNAKE_SEGMENTS = 4
    SNAKE_SEGMENT_WIDTH = 20
    DIRECTION_OFFSET_MAP = {
        "u": (0, SNAKE_SEGMENT_WIDTH),
        "d": (0, -1 * SNAKE_SEGMENT_WIDTH),
        "l": (-1 * SNAKE_SEGMENT_WIDTH, 0),
        "r": (SNAKE_SEGMENT_WIDTH, 0)
    }
    DEFAULT_SPEED = "normal"
    snake_segment_positions = []
    snake = []
    current_direction = "r"

    def __init__(self):
        for segment in range(self.NUMBER_OF_SNAKE_SEGMENTS):
            segment_color = "red" if segment == self.NUMBER_OF_SNAKE_SEGMENTS -1 else "yellow" if segment == 0 else "white"
            self.create_snake_segment(segment_color)
            self.snake_segment_positions.append((segment * self.SNAKE_SEGMENT_WIDTH * -1, 0))

    def create_snake_segment(self, color):
        snake_segment = Turtle(shape="square")
        snake_segment.color(color)
        snake_segment.penup()
        snake_segment.speed(self.DEFAULT_SPEED)
        self.snake.append(snake_segment)

    def move_snake(self, direction):

        self.current_direction = direction if direction is not None else self.current_direction

        # extract offset from the map based on direction
        offset = self.DIRECTION_OFFSET_MAP[direction]

        # generate the new head
        head = tuple(map(sum, zip(self.snake_segment_positions[0], offset)))

        # insert new head into initial position, pop off former position of tail
        self.snake_segment_positions.insert(0, head)
        self.snake_segment_positions.pop()

        # set position of each snake segment ( per positions list )
        for index in range(len(self.snake)):
            self.snake[index].setpos(self.snake_segment_positions[index])

    def head_position(self):
        return self.snake_segment_positions[0]
