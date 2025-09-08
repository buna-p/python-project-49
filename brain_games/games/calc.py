import prompt, random


def task():
    print('What is the result of the expression?')


def operation_random() -> str:
    operations = ["+", "-", "*"]
    return random.choice(operations)


def get_answer_user() -> tuple[str, str]:
    number1, number2 = random.randint(0, 100), random.randint(0, 100)
    operation = operation_random()
    question = f"{number1} {operation} {number2}"
    print(f"Question: {question}")
    answer_user = prompt.string("Your answer: ")
    return question, answer_user


def get_correct_answer(question: str) -> int:
    question_transformed = question.split()
    number1, operation, number2 = question_transformed
    match operation:
        case "-":
            return int(number1) - int(number2)
        case "+":
            return int(number1) + int(number2)
        case "*":
            return int(number1) * int(number2)