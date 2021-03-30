from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions = question_data

question_bank = []

for quest in questions:
    question_bank.append(Question(quest['text'], quest['answer']))

quiz = QuizBrain(question_bank)

while quiz.stii_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.get_score()}/{quiz.get_question_number()}")