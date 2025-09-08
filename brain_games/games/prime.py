import prompt, random


def task():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def get_answer_user() -> tuple[str, str]:
    number = random.randint(2, 100)
    question = number
    print(f"Question: {question}")
    answer_user = prompt.string("Your answer: ")
    return question, answer_user


def get_correct_answer(question: str) -> str:
    number = int(question)
    divider = 2
    while divider <= number:
        if number == divider:
            return 'yes'
        elif number % divider != 0:
            divider += 1
        else:
            return 'no'