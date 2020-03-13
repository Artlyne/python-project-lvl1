import random

game_task = 'What number is missing in the progression?'


def random_progression():
    progression_start = random.randint(1, 50)
    progression_step = random.randint(1, 10)
    progression = []

    i = 0
    while i != 10:
        progression.append(progression_start)
        progression_start += progression_step
        i += 1

    return progression


def ask():
    progression = random_progression()  # len of progression is 10
    extractable_number = random.randint(0, 9)  # index of this number
    correct_answer = progression[extractable_number]
    progression[extractable_number] = '..'

    question = ''
    for i in range(len(progression)):
        question += f'{progression[i]} '

    return question, correct_answer
