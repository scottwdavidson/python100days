from turtle import Screen
from etchy import Etchy


if __name__ == '__main__':
    # setup the screen
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.listen()

    # setup etchy ( the turtle )
    etchy = Etchy()

    # map key to functions
    screen.onkey(etchy.move_forwards, "w")
    screen.onkey(etchy.move_backwards, "s")
    screen.onkey(etchy.move_left, "a")
    screen.onkey(etchy.move_right, "d")
    screen.onkey(etchy.clear, "c")


    screen.exitonclick()
