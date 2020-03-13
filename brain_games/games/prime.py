import random


game_task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_number_prime(number):
    divisor = 2
    while number % divisor != 0:
        divisor += 1
    if number == divisor:
        return True
    else:
        return False


def ask():
    number = random.randint(2, 101)
    question = number
    correct_answer = 'yes' if is_number_prime(number) else 'no'
    return question, correct_answer
