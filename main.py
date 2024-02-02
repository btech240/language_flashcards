import random
from tkinter import *

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

# Read data from csv file, put into pandas dataframe
df = pd.read_csv("data/french_words.csv")
# Convert the dataframe to python dictionary
to_learn = df.to_dict("records")
current_card = {}
known_unknown = {"known": 0, "unknown": 0}


def next_card():
    # Generate a new random word on the flash card
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    # Show the english translation of the current french word

    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    global known_unknown
    known_unknown["known"] += 1
    print(known_unknown)
    next_card()


def is_unknown():
    global known_unknown
    known_unknown["unknown"] += 1
    print(known_unknown)
    next_card()


# Initialize the window for the application
window = Tk()
window.title("Language Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Create the canvas for the card front
canvas = Canvas(width=800, height=526,
                background=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=(
    "Arial", 40, "italic"), fill="#000000")
card_word = canvas.create_text(400, 263, text="", font=(
    "Arial", 60, "bold"), fill="#000000")
canvas.grid(column=0, row=0, columnspan=2)

# Create "know" button
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(
    image=cross_image, highlightthickness=0, command=is_unknown)
unknown_button.grid(column=0, row=1)

# Create "dont know" button
check_image = PhotoImage(file="images/right.png")
known_button = Button(
    image=check_image, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

next_card()

# Window mainloop to keep GUI display open
window.mainloop()
