from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TURNS = ("RIGHT", "LEFT")
turn_index = 0


def right_paddle_is_current_turn():
    return turn_index == 0


def ball_connects_with_paddle(paddle_x_coordinate_range, paddle_y_coordinate_range):
    return (paddle_x_coordinate_range[0] <= ball.xcor() <= paddle_x_coordinate_range[1] and
            paddle_y_coordinate_range[0] <= ball.ycor() <= paddle_y_coordinate_range[1])


def current_paddle_x_coordinate_range():
    if right_paddle_is_current_turn():
        return right_paddle.xcor() - 20, right_paddle.xcor() + 10
    else:
        return left_paddle.xcor() -10, left_paddle.xcor() +20

def current_paddle_y_coordinate_range():
    if right_paddle_is_current_turn():
        return right_paddle.ycor() - 50, right_paddle.ycor() + 50
    else:
        return left_paddle.ycor() - 50, left_paddle.ycor() + 50


def ball_is_on_court():
    return left_paddle.xcor() < ball.xcor() < right_paddle.xcor()
def switch_turns():
    new_turn_index = (turn_index + 1) % 2
    print(f"Switched Turns: {TURNS[new_turn_index]}")
    return new_turn_index

# setup the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("PONG")
screen.tracer(0)

minimum_y_coordinate = -1 * int(SCREEN_HEIGHT / 2) + 10
maximum_y_coordinate = int(SCREEN_HEIGHT / 2) - 10

left_paddle = Paddle(-1 * int(SCREEN_WIDTH / 2) + 40, 0, -1 * int(SCREEN_HEIGHT / 2), int(SCREEN_HEIGHT / 2))
right_paddle = Paddle(int(SCREEN_WIDTH / 2) - 40, 0, -1 * int(SCREEN_HEIGHT / 2), int(SCREEN_HEIGHT / 2))
ball = Ball()

screen.onkey(right_paddle.paddle_up, "Up")
screen.onkey(right_paddle.paddle_down, "Down")
screen.onkey(left_paddle.paddle_up, "w")
screen.onkey(left_paddle.paddle_down, "s")
screen.listen()

game_is_on = True
while game_is_on:

    # move the ball
    ball.move()
    screen.update()

    # check for top / bottom bounces
    if ball.ycor() >= maximum_y_coordinate - 10 or ball.ycor() <= minimum_y_coordinate + 10:
        ball.bounce_y_direction()

    # check for connection with paddle
    if ball_connects_with_paddle(current_paddle_x_coordinate_range(), current_paddle_y_coordinate_range()):
        ball.bounce_x_direction()
        turn_index = switch_turns()

    # check for ball off court
    if not ball_is_on_court():
        game_is_on = False
        turn_index = switch_turns()
        # give score to side w/ turn and serve again (towards the point winner)

    time.sleep(0.1)

screen.exitonclick()
