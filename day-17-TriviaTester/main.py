from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

quiz_bank = []

for ques_dict in question_data:
    text = ques_dict["text"]
    answer = ques_dict["answer"]
    new_question = Question(text, answer)
    quiz_bank.append(new_question)

quiz_brain = QuizBrain(quiz_bank)

while not quiz_brain.is_end():
    quiz_brain.next_question()

print(f"You have won the game. ")
print(f"FinalScore = {quiz_brain.score}/{quiz_brain.ques_index}")



