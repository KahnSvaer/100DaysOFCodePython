import random


class QuizBrain:

    def __init__(self, q_list):
        self.question_bank = q_list
        self.question_num = 0
        self.score = 0
        random.shuffle(self.question_bank)

    def next_question(self):
        if not self.still_has_questions():
            print("Questions_completed")
            return None
        else:
            question = self.question_bank[self.question_num]
            self.question_num += 1
            user_answer = input(f"Q{self.question_num}. {question.text} (True/False)? ")
            self.check_answer(question, user_answer)

    def still_has_questions(self):
        return self.question_num < len(self.question_bank)

    def check_answer(self, question, ans):
        if ans.strip().lower() == question.answer.strip().lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong!")
        print(f"The correct answer is {question.answer}")
        print(f"The currant score is: {self.score}/{self.question_num}")
        print("\n")
