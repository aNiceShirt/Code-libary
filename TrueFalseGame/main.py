from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# Generating question bank
question_bank = []
for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions() == True:
    quiz.next_question()

print(f"You have completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")