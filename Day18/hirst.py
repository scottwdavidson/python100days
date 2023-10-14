import colorgram
from turtle import Turtle, Screen
import random


def extract_colors(image_name, desired_number_of_colors, remove_background):
    extracted_colorgram = colorgram.extract(image_name, desired_number_of_colors)
    # print(f"{extracted_colorgram}")
    extracted_colors_result = []
    for colorgram_item in extracted_colorgram:
        if remove_background and colorgram_item.proportion > 0.30:
            # print("skipping background ...")
            continue
        # if (colorgram_item.rgb.r + colorgram_item.rgb.b + colorgram_item.rgb.b) > 660:
        #     print(f"skipping very light color {colorgram_item}")
        #     continue
        extracted_color_named_tuple = colorgram_item.rgb
        extracted_colors_result.append(
            (extracted_color_named_tuple.r, extracted_color_named_tuple.g, extracted_color_named_tuple.b))
    return extracted_colors_result


if __name__ == '__main__':

    # Get colors to be used
    # TODO: get colors in correct proportion to the originally painting
    extracted_colors = extract_colors("hirst_image.gif", 30, True)
    # print(f"extracted_colors: {extracted_colors}")

    # Setup hirst the turtle
    hirst = Turtle()
    screen = Screen()
    screen.colormode(255)
    hirst.speed("fastest")
    width, height = screen.window_width(), screen.window_height()
    hirst.penup()
    hirst.left(90)
    hirst.forward(int(height/2) - 50)
    hirst.left(90)
    hirst.forward(int(width/2) - 50)
    hirst.left(180)
    hirst.pendown()

    # Generate the "grid"
    NUMBER_OF_COLUMNS = 18
    NUMBER_OF_ROWS = 18
    CIRCLE_RADIUS = 6
    CIRCLE_SPACING = 6

    for row in range(NUMBER_OF_ROWS):

        for col in range(NUMBER_OF_COLUMNS):

            # draw circle
            pen_color = random.choice(extracted_colors)
            # print(f"pen_color: {pen_color}")
            hirst.fillcolor(pen_color)
            hirst.begin_fill()
            hirst.pencolor(pen_color)
            hirst.circle(CIRCLE_RADIUS)
            hirst.end_fill()

            # move to right spacing ( plus radius )
            hirst.penup()
            hirst.forward(CIRCLE_SPACING + 2 * CIRCLE_RADIUS)
            hirst.pendown()


        # reset point to next row: down spacing + radius, left full distance
        hirst.penup()
        hirst.right(90)
        hirst.forward(CIRCLE_SPACING + 2 * CIRCLE_RADIUS)
        hirst.right(90)
        hirst.forward(NUMBER_OF_COLUMNS * (CIRCLE_RADIUS + 2 * CIRCLE_RADIUS))
        hirst.right(180)
        hirst.pendown()

    screen.exitonclick()

