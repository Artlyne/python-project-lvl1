import random
import operator

game_task = 'What is the result of the expression?'


def ask():
    math_operators = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    random_operator = random.choice(['+', '-', '*'])
    question = f'{number1} {random_operator} {number2}'
    correct_answer = math_operators[random_operator](number1, number2)
    return question, str(correct_answer)
