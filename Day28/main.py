import math
from tkinter import *
from math import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
SINGLE_CHECKMARK = "✓"
repetition = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    root.after_cancel(timer)
    canvas.itemconfig(timer_text, text="")
    title_label.config(text="Timer")
    global repetition
    repetition = 0
    checkmarks_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Pomodoro")
root.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


# start timer
def start_timer():
    work_seconds = 5
    short_break_seconds = 3
    long_break_seconds = 8
    global repetition

    if repetition == 0:
        checkmarks_label.config(text="")

    repetition += 1
    if repetition % 8 == 0:
        title_label.config(text="BREAK", fg=RED)
        count_down(long_break_seconds)

        # reset repetition and check marks
        # reset_core_fields()
        repetition = 0

    elif repetition % 2 == 0:
        title_label.config(text="BREAK", fg=PINK)
        count_down(short_break_seconds)
    else:
        title_label.config(text="WORK", fg=GREEN)
        count_down(work_seconds)


def two_digit_number_presentation(minute_or_second_duration):
    if minute_or_second_duration < 10:
        return f"0{minute_or_second_duration}"
    else:
        return minute_or_second_duration


def checkmarks_presentation(number_of_checkmarks):
    checkmarks = ""
    for checkmark in range(number_of_checkmarks):
        checkmarks += SINGLE_CHECKMARK
    return checkmarks


def count_down(duration_in_seconds):
    minutes_duration_presentation = two_digit_number_presentation(math.floor(duration_in_seconds / 60))
    seconds_duration_presentation = two_digit_number_presentation(duration_in_seconds % 60)
    timer_text_presentation = f"{minutes_duration_presentation}:{seconds_duration_presentation}"
    canvas.itemconfig(timer_text, text=f"{timer_text_presentation}")

    if duration_in_seconds > 0:
        global timer
        timer = root.after(1000, count_down, duration_in_seconds - 1)
    else:
        if (repetition + 1) % 2 == 0:
            checkmarks_label.config(text=checkmarks_presentation(int((repetition + 1) / 2)))
        start_timer()


# checkmarks label
checkmarks_label = Label(text="", bg=YELLOW, fg=GREEN, highlightthickness=0)
checkmarks_label.grid(row=3, column=1)

# title label
title_label = Label(text="Timer", font=(FONT_NAME, 54), bg=YELLOW, fg=GREEN)
title_label.grid(row=0, column=1)

# start button
start_button = Button(text="Start", font=(FONT_NAME, 10), bg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

# start button
reset_button = Button(text="Reset", font=(FONT_NAME, 10), bg=YELLOW, highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

root.mainloop()
