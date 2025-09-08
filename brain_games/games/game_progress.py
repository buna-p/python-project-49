def is_answer_user_correct(answer_user: str, correct_answer: int) -> bool:
    if answer_user.lower() == str(correct_answer).lower():
        return True
    return False