from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_count = None

# ---------------------------- TIMER RESET ------------------------------- #
def button_reset(*args):
    global reps
    window.after_cancel(timer_count)
    reps = 0
    title_label.config(text="Timer", font=(FONT_NAME, 42, "bold"), bg=YELLOW, fg=GREEN)
    canvas.itemconfig(timer, text="00:00")
    check.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def button_start(*args):
    global reps
    reps += 1
    work_sec = WORK_MIN * 1
    short_sec = SHORT_BREAK_MIN * 1
    long_sec = LONG_BREAK_MIN * 1

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        count_down(work_sec, reps)
        title_label.config(text="Work!", font=(FONT_NAME, 42, "bold"), bg=YELLOW, fg=GREEN)
    elif reps == 2 or reps == 4 or reps == 6:
        count_down(short_sec, reps)
        title_label.config(text="Break!", font=(FONT_NAME, 42, "bold"), bg=YELLOW, fg=PINK)
    elif reps == 8:
        count_down(long_sec, reps)
        title_label.config(text="Rest!", font=(FONT_NAME, 42, "bold"), bg=YELLOW, fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count, reps):


    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_count
        timer_count = window.after(1000, count_down, count - 1, reps)
        print(reps)
    else:
        button_start()
        marks = ""
        work_sessions = math.floor(reps/2)
        for x in range(work_sessions):
            marks += "✔"
            check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", font=(FONT_NAME, 42, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo_tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo_tomato)
canvas.grid(column=1, row=1)
timer = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

button = Button(text="Start", command=button_start)
button.grid(column=0, row=3)

button = Button(text="Reset", command=button_reset)
button.grid(column=3, row=3)

check = Label(font=(FONT_NAME, 16), bg=YELLOW, fg=GREEN)
check.grid(column=1, row=4)

window.mainloop()
