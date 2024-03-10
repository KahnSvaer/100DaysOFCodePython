from random import shuffle


class QuizBrain:
    def __init__(self, question_bank):
        self.question_bank = question_bank
        shuffle(self.question_bank)
        self.total_questions = len(self.question_bank)
        self.ques_index = 0
        self.score = 0

    def next_question(self):
        current_question = self.question_bank[self.ques_index]
        self.ques_index += 1
        user_response = input(f"Q.{self.ques_index}: {current_question.text} (True/False): ").strip().lower()
        return self._answer_correct(current_question, user_response)

    def _answer_correct(self, question, answer):
        is_correct = (question.answer.lower() == answer.lower())
        self.score += is_correct
        print(f"The answer was {question.answer}")
        print(f"Your Current Score is: {self.score}/{self.ques_index}\n")
        return is_correct

    def is_end(self):
        return self.ques_index == self.total_questions
