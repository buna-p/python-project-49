import random

import prompt


def task():
    print('Find the greatest common divisor of given numbers.')


def get_answer_user() -> tuple[str, str]:
    number1, number2 = random.randint(0, 100), random.randint(0, 100)
    question = f"{number1} {number2}"
    print(f"Question: {question}")
    answer_user = prompt.string("Your answer: ")
    return question, answer_user


def get_correct_answer(question: str) -> int:
    question_transformed = question.split()
    number1_str, number2_str = question_transformed
    number1, number2 = int(number1_str), int(number2_str)
    if number2 > number1:
        number2, number1 = number1, number2
    if number1 == number2 or number2 == 0:
        return number1
    while number2 > 0:
        remainder = number1 % number2
        number1 = number2
        number2 = remainder
    return number1