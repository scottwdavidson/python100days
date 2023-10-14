import random
from turtle import Turtle, Screen

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def random_color_255():
    red = random.randint(0, 0xFF)
    green = random.randint(0, 0xFF)
    blue = random.randint(0, 0xFF)
    return (red,green,blue)

def draw_spiro_circle(turtle, radius, heading):
    color = random_color_255()
    turtle.pencolor(color)
    turtle.setheading(heading)
    turtle.circle(radius)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    RADIUS = 75
    HEADING_DELTA = 5

    screen = Screen()
    screen.colormode(255)
    tim = Turtle()
    tim.speed("fastest")

    current_heading = tim.heading()
    while current_heading < 360:
        draw_spiro_circle(tim,RADIUS, current_heading)
        current_heading += HEADING_DELTA

    screen.exitonclick()