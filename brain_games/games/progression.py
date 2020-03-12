import random

game_task = 'What number is missing in the progression?'


def random_progression():
    progression_start = random.randint(1, 50)
    progression_step = random.randint(1, 10)
    progression = [progression_start]
    next_number = progression_start
    i = 1
    while i != 10:
        next_number += progression_step
        progression.append(next_number)
        i += 1
    return progression


def ask():
    question = None
    correct_answer = None
    return question, correct_answer
