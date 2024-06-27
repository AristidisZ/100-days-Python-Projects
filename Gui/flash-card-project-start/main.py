from tkinter import *
import pandas as pd
import random

current_card = {}
to_learn = {}

try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# print(type(to_learn))


def next_word():
    global current_card, flipt_timer
    window.after_cancel(flipt_timer)
    current_card = random.choice(to_learn)
    print(current_card)
    canvas.itemconfig(up_text, text="French", fill="black")
    canvas.itemconfig(down_text, text=current_card["French"], fill="black")
    flipt_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(up_text, text="English", fill="white")
    canvas.itemconfig(down_text, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=back_image)


def is_known():
    to_learn.remove(current_card)
    data_to_learn = pd.DataFrame(to_learn)
    data_to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_word()


# UI
# --------------------------------------------------------


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flipt_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 260, image=front_image)
up_text = canvas.create_text(400, 150, text="French", fill="black", font=("Ariel", 40, "bold"))
down_text = canvas.create_text(400, 263, text="trouve", fill="black", font=("Ariel", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

my_no = PhotoImage(file="./images/wrong.png")
button_no = Button(image=my_no, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_word)
button_no.grid(column=0, row=1)

my_yes = PhotoImage(file="./images/right.png")
button_yes = Button(image=my_yes, bg=BACKGROUND_COLOR, highlightthickness=0, command=is_known)
button_yes.grid(column=1, row=1)

next_word()

window.mainloop()
