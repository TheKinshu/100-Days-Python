class QuizBrain():
    def __init__(self, questionsList) -> None:
        self.question_number = 0
        self.questions_list = questionsList
        self.score = 0

    def next_question(self):
        questionNum = self.question_number
        self.question_number += 1
        currentQuestion = self.questions_list[questionNum]

        user_answer = input(f"Q.{questionNum + 1}: {currentQuestion.text}. (True/False)")
        self.check_answer(user_answer, currentQuestion.answer)
    
    def get_score(self):
        return self.score

    def get_question_number(self):
        return self.question_number


    def stii_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, answer, current_question_answer):
        

        if answer.lower() == current_question_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct asnwer was: {current_question_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
