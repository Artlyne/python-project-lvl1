import random
import operator

GAME_TASK = 'What is the result of the expression?'
MATH_OPERATORS = ('+', operator.add), ('-', operator.sub), ('*', operator.mul)


def generate_round():
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    symbol, math_operator = random.choice(MATH_OPERATORS)
    question = f'{number1} {symbol} {number2}'
    correct_answer = str(math_operator(number1, number2))
    return question, correct_answer
