import random

GAME_TASK = 'Answer "yes" if number even otherwise answer "no".'


def generate_round():
    question = random.randint(1, 100)
    is_number_even = (question % 2 == 0)
    correct_answer = 'yes' if is_number_even else 'no'
    return question, correct_answer
