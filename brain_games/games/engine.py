from brain_games.cli import welcome_user
from brain_games.games.game_progress import is_answer_user_correct
from brain_games.greet import greet
from brain_games.win import win


def engine(game):
    greet()
    name = welcome_user()
    game.task()
    counter_correct_answer = 0
    while counter_correct_answer < 3:
        question, answer_user = game.get_answer_user()
        correct_answer = game.get_correct_answer(question)
        level_up = is_answer_user_correct(answer_user, correct_answer)
        if not level_up:
            print(
            f"'{answer_user}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.\nLet's try again, {name}!"
        )
            break
        print("Correct!")
        counter_correct_answer += 1
    if counter_correct_answer == 3:
        win(name)