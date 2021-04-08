from tkinter import *
import pandas, random

BACKGROUND_COLOR = "#B1DDC6"
LANFONT = ("Ariel", 40, "italic")
WORDFONT = ("Ariel", 60, "bold")
LANGUAGE1 = 'French'
LANGUAGE2 = 'English'

timer = None
currentWord = None


def wordsToLearn():
    try:
        data = pandas.read_csv("./Day31/data/words_to_learn.csv")
        return data.to_dict(orient="records")
    except Exception:
        data = pandas.read_csv("./Day31/data/french_words.csv")
        return data.to_dict(orient="records")

def flipWord(english, count):
    global timer
    if count > 0:
        timer = window.after(1000, flipWord, english, count - 1)
    else:
        window.after_cancel(timer)
        canvas.itemconfig(languageType, text=LANGUAGE2, fill='white')
        canvas.itemconfig(wordList, text=english, fill='white')
        canvas.itemconfig(canvasImage, image=cardBack)


def chooseWord():
    global currentWord
    try:
        currentWord = random.choice(french_dict)
    except IndexError:
        canvas.itemconfig(languageType, text="Completed", fill='black')
        canvas.itemconfig(wordList, text="Congratulation, you have learn all \nthe words in this list!", fill='black', font=("Ariel", 30, "bold"))
    else:
        french_word = currentWord[LANGUAGE1]
        english_word = currentWord[LANGUAGE2]
        canvas.itemconfig(canvasImage, image=cardFront)
        canvas.itemconfig(languageType, text=LANGUAGE1, fill='black')
        canvas.itemconfig(wordList, text=french_word, fill='black')
        flipWord(english_word, 3)

def knowWord():
    global currentWord
    french_dict.remove(currentWord)

    df = pandas.DataFrame(french_dict)
    df.to_csv("./Day31/data/words_to_learn.csv",index=False)

    chooseWord()    

french_dict = wordsToLearn()


window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Image
x_button_image = PhotoImage(file="./Day31/images/wrong.png")
check_button_image = PhotoImage(file="./Day31/images/right.png")
cardBack = PhotoImage(file="./Day31/images/card_back.png")
cardFront = PhotoImage(file="./Day31/images/card_front.png")

# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvasImage = canvas.create_image(400,263,image=cardFront)
languageType = canvas.create_text(400,150,text=LANGUAGE1, font=LANFONT)
wordList = canvas.create_text(400,263,text="Trouve", font=WORDFONT)
canvas.grid(column=0, row=0, columnspan=2)
chooseWord()

# Button
wrongBtn = Button(image=x_button_image, highlightthickness=0, borderwidth=0, command=chooseWord)
wrongBtn.grid(column=0,row=1)

rightBtn = Button(image=check_button_image, highlightthickness=0, borderwidth=0, command=knowWord)
rightBtn.grid(column=1,row=1)

window.mainloop()