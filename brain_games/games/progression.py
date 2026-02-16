import random

import prompt


RANGE_1 = (0, 100)
RANGE_2 = (1, 10)
RANGE_3 = (0, 11)
RANGE_4 = (1, 9)
RANGE_5 = (0, 10)


def task():
    print('What number is missing in the progression?')


def progression_numbers() -> list:
    start = random.randint(*RANGE_1)
    step = random.randint(*RANGE_2)
    progression = []
    for i in range(*RANGE_3):
        currentElement = str(start + i * step)
        progression.append(currentElement)
    return progression


def get_answer_user() -> tuple[str, str]:
    index = random.randint(*RANGE_4)
    progression = progression_numbers()
    progression[index] = '..'
    question = f"{' '.join(progression)}"
    print(f"Question: {question}")
    answer_user = prompt.string("Your answer: ")
    return question, answer_user


def get_correct_answer(question: str) -> int:
    progression = question.split()
    index_x = progression.index('..')
    for i in range(len(progression) - 1):
        if progression[i] != '..' and progression[i + 1] != '..':
            step = int(progression[i + 1]) - int(progression[i])
            pass
    if index_x > 0:
        return int(progression[index_x - 1]) + step
    else:
        return int(progression[index_x + 1]) - step