import random

GAME_TASK = 'Find the greatest common divisor of given numbers.'


# Euclidean algorithm
def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def generate_round():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    question = f'{number1} {number2}'
    correct_answer = str(gcd(number1, number2))
    return question, correct_answer
