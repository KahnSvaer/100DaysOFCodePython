from question_model import QuestionModel
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for questions in question_data:
    question_text = questions["question"]
    question_answer = questions["correct_answer"]
    new_question = QuestionModel(question_text, question_answer)
    question_bank.append(new_question)

quizz_brain = QuizBrain(q_list=question_bank)
while quizz_brain.still_has_questions():
    quizz_brain.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quizz_brain.score}/{quizz_brain.question_num}")
