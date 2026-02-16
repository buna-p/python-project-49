import random

import prompt


RANGE = (1, 100)


def task():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def get_answer_user() -> tuple[str, str]:
    number = random.randint(*RANGE)
    question = number
    print(f"Question: {question}")
    answer_user = prompt.string("Your answer: ")
    return question, answer_user


def get_correct_answer(question: str) -> str:
    question_transformed = int(question)
    if question_transformed % 2 == 0:
        return 'yes'
    return 'no'