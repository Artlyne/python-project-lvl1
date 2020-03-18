import random

GAME_TASK = 'Answer "yes" if number even otherwise answer "no".'


def ask():
    number = random.randint(1, 100)
    question = number
    is_number_even = (number % 2 == 0)
    correct_answer = 'yes' if is_number_even else 'no'
    return question, correct_answer
