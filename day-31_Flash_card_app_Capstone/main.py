BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random
from os.path import exists

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card  = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French')
    canvas.itemconfig(card_word, text=current_card['French'])
    canvas.itemconfig(card_image, image=card_front_image)
    flip_timer = window.after(3000, flip_card)  

def flip_card():
    canvas.itemconfig(card_title, text='English')
    canvas.itemconfig(card_word, text=current_card['English'])
    canvas.itemconfig(card_image, image=card_back_image)

def card_known():
    to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv("day-31_Flash_card_app_Capstone/data/to_learn.csv", index=False, mode="w") # index=False stops the addition of the index to the dataframe

print("running program")
## Window set-up
window = Tk()
window.title("Flash Cards App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

try:
    data = pandas.read_csv("day-31_Flash_card_app_Capstone/data/to_learn.csv")

except FileNotFoundError:
    original_data = pandas.read_csv("day-31_Flash_card_app_Capstone/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

current_card = {}   
flip_timer = window.after(3000, flip_card)

## Card images
card_front_image = PhotoImage(file= "day-31_Flash_card_app_Capstone/images/card_front.png")
card_back_image = PhotoImage(file= "day-31_Flash_card_app_Capstone/images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=card_front_image)
canvas.grid(column=0, row=0, columnspan=2)

## Buttons
known_image = PhotoImage(file= "day-31_Flash_card_app_Capstone/images/right.png")
known_button = Button(image=known_image, command=card_known, highlightthickness=0, bg=BACKGROUND_COLOR)
known_button.grid(column = 1, row =1)

unknown_image = PhotoImage(file= "day-31_Flash_card_app_Capstone/images/wrong.png")
unknown_button = Button(image=unknown_image, command=next_card, highlightthickness=0, bg=BACKGROUND_COLOR)
unknown_button.grid(column= 0, row =1)


## Text
card_title = canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

next_card()


window.mainloop()