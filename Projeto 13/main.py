from question_model import Question
from data import question_data

question_bank = []

for x in question_data:
    question_text = x["text"]
    question_answer = x["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

print(question_bank[0].text,question_bank[0].answer)