from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface():
    
    def __init__(self, quiz:QuizBrain) -> None:
        self.quiz = quiz
        self.score = 0

        self.window = Tk()
        self.window.title("Qizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.checkImage = PhotoImage(file="./Day34/images/true.png")
        self.falseImage = PhotoImage(file="./Day34/images/false.png")


        # Canvas
        self.canvas = Canvas(width=300, height= 250)
        self.question = self.canvas.create_text(150,125, text="Random Text", font=FONT, fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Label
        self.scoreLabel = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg='white')
        self.scoreLabel.grid(column=1,row=0)

        # Button
        self.trueButton = Button(image=self.checkImage, highlightthickness=0, bg=THEME_COLOR, command=self.guessTrue)
        self.trueButton.grid(column=0, row=2)
        
        self.falseutton = Button(image=self.falseImage, highlightthickness=0, bg=THEME_COLOR, command=self.guessFalse)
        self.falseutton.grid(column=1, row=2)
        
        self.getNextQuestion()

        self.window.mainloop()

    def getNextQuestion(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=question)
        else:
            self.canvas.itemconfig(self.question, text="You've reach the end of the quiz!")
            self.trueButton.config(state="disabled")
            self.falseutton.config(state="disabled")

    def guessTrue(self):
        checkAnswer = self.quiz.check_answer('True')
        self.giveFeedback(checkAnswer)

    def guessFalse(self):
        checkAnswer = self.quiz.check_answer('False')
        self.giveFeedback(checkAnswer)

    def giveFeedback(self, checkAnwer):
        if checkAnwer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.score = self.quiz.score
        self.scoreLabel.config(text=f"Score: {self.score}")
        self.window.after(1000, self.getNextQuestion)


        