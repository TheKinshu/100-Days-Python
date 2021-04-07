from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
LANFONT = ("Ariel", 40, "italic")
WORDFONT = ("Ariel", 60, "bold")

data = pandas.read_csv("./Day31/data/french_words.csv")
french_dict = data.to_dict(orient="records")

window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

cardBack = PhotoImage(file="./Day31/images/card_back.png")
cardFront = PhotoImage(file="./Day31/images/card_front.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_image(400,263,image=cardFront)
languageType = canvas.create_text(400,150,text="French", font=LANFONT)
wordList = canvas.create_text(400,263,text="Trouve", font=WORDFONT)
canvas.grid(column=0, row=0, columnspan=2)

# Button
x_button_image = PhotoImage(file="./Day31/images/wrong.png")
check_button_image = PhotoImage(file="./Day31/images/right.png")

wrongBtn = Button(image=x_button_image, highlightthickness=0, borderwidth=0)
wrongBtn.grid(column=0,row=1)

rightBtn = Button(image=check_button_image, highlightthickness=0, borderwidth=0)
rightBtn.grid(column=1,row=1)

window.mainloop()