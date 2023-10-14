from snake import Snake
from breadcrumb import Breadcrumb
from controller import Controller
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# create the snake and breadcrumb
snake = Snake()
breadcrumb = Breadcrumb(SCREEN_HEIGHT, SCREEN_WIDTH)

# use the Controller to set up & control the screen
controller = Controller(SCREEN_HEIGHT, SCREEN_WIDTH, snake, breadcrumb)

game_in_progress = True
score = 0
while game_in_progress:
    game_in_progress = controller.move_snake()
    time.sleep(0.1)
