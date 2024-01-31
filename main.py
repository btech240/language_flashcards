from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# Initialize the window for the application
window = Tk()
window.title("Language Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Create the canvas for the card front
canvas = Canvas(width=800, height=526,
                background=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front)
canvas.create_text(400, 150, text="Title", font=(
    "Arial", 40, "italic"), fill="#000000")
canvas.create_text(400, 263, text="word", font=(
    "Arial", 60, "bold"), fill="#000000")
canvas.grid(column=0, row=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0)
unknown_button.grid(column=0, row=1)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0)
known_button.grid(column=1, row=1)


# Window mainloop to keep GUI display open
window.mainloop()
