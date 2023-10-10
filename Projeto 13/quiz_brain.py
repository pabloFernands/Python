class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_question(self):
        count = len(self.question_list)
        return self.question_number < count

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True or False)? ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer , correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Você acertou. You got it right!")
            self.score += 1
        else:
            print("Você errou. That's wrong")
        print(f"A resposta correta é: {correct_answer}. The corre answer was: {correct_answer}")
        print(f"Yout score is: {self.score}/{self.question_number}\n")
