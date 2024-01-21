import os
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


#--------------------------------Read-Words-----------------------------#

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
    # Criou um dictionary de cada linha do arquivo CSV usando orient para facilitar a manipulação.


def read_words_french():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_text, text=current_card["French"], fill="black")
    canvas.itemconfig(card_image, image=IMAGE_FRONT_CARD)
    flip_timer = window.after(3000, func=read_words_english)
    print(current_card)



    #print(french_word)
    return

def read_words_english():
    canvas.itemconfig(card_image, image=IMAGE_BACK_CARD)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=current_card["English"], fill="white")
    return

def is_known():
    to_learn.remove(current_card)
    #print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    read_words_french()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=read_words_english)
IMAGE_FRONT_CARD = PhotoImage(file="images/card_front.png")
IMAGE_BACK_CARD = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=IMAGE_FRONT_CARD)
canvas.config(background=BACKGROUND_COLOR)
card_title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
card_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=read_words_french)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

read_words_french()

window.mainloop()

