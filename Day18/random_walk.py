import random
from turtle import Turtle, Screen

def random_color_255():
    red = random.randint(0, 0xFF)
    green = random.randint(0, 0xFF)
    blue = random.randint(0, 0xFF)
    return (red,green,blue)

def random_heading(turtle):
    DIRECTION_CHANGES = [0, 90, 180, 270]
    current_heading = turtle.heading()
    new_heading = random.choice(DIRECTION_CHANGES)
    while abs(new_heading - current_heading) == 180:
        new_heading = random.choice(DIRECTION_CHANGES)
    return new_heading
def draw_random_step(turtle, step_length):

    # randomly determine direction
    direction_change = random_heading(turtle)
    color = random_color_255()
    turtle.pencolor(color)
    turtle.setheading(direction_change)
    turtle.forward(step_length)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    LENGTH = 20
    PEN_SIZE_WIDTH = 10
    TURTLE_SPEED = 6

    screen = Screen()
    screen.colormode(255)
    tim = Turtle()
    tim.pensize(PEN_SIZE_WIDTH)
    tim.speed(TURTLE_SPEED)
    for _ in range(200):
        draw_random_step(tim,LENGTH)


    screen.exitonclick()