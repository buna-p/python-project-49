import random

import prompt


def task():
    print('What number is missing in the progression?')


def progression_numbers() -> list:
    start = random.randint(0, 100)
    step = random.randint(1, 10)
    progression = []
    for i in range(0, 11):
        currentElement = str(start + i * step)
        progression.append(currentElement)
    return progression


def get_answer_user() -> tuple[str, str]:
    index = random.randint(1, 9)
    progression = progression_numbers()
    progression[index] = '..'
    question = f"{' '.join(progression)}"
    print(f"Question: {question}")
    answer_user = prompt.string("Your answer: ")
    return question, answer_user


def get_correct_answer(question: str) -> int:
    progression = question.split()
    index_x = progression.index('..')
    if index_x >= len(progression) // 2:
        step = int(progression[1]) - int(progression[0])
        start = int(progression[0])
        progression_with_x = []
        for i in range(0, 10):
            currentElement = start + i * step
            progression_with_x.append(currentElement)
        return progression_with_x[index_x]
    else:
        step = int(progression[index_x + 2]) - int(progression[index_x + 1])
        finish = int(progression[9])
        progression_with_x = []
        for i in range(0, 10):
            currentElement = finish - i * step
            progression_with_x.insert(0, currentElement)
        return progression_with_x[index_x]