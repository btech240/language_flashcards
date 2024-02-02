import random
from tkinter import *

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

# Read data from csv file, put into pandas dataframe
df = pd.read_csv("data/french_words.csv")
# Convert the dataframe to python dictionary
to_learn = df.to_dict("records")

# Initialize the window for the application
window = Tk()
window.title("Language Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Create the canvas for the card front
canvas = Canvas(width=800, height=526,
                background=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=(
    "Arial", 40, "italic"), fill="#000000")
card_word = canvas.create_text(400, 263, text="", font=(
    "Arial", 60, "bold"), fill="#000000")
canvas.grid(column=0, row=0, columnspan=2)


def next_card():
    # Generate a new random word on the flash card
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])


# Create "know" button
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(
    image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

# Create "dont know" button
check_image = PhotoImage(file="images/right.png")
known_button = Button(
    image=check_image, highlightthickness=0, command=next_card)
known_button.grid(column=1, row=1)

next_card()

# Window mainloop to keep GUI display open
window.mainloop()
