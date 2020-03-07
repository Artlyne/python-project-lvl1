from random import randint
from cli import welcome_user


def game_even():
    print('Welcome to the Brain Games!\n'
          'Answer "yes" if number even otherwise answer "no".\n')

    name = welcome_user()[0]
    print('\n')

    for answer in range(3):
        random_number = randint(1, 100)
        is_number_even = (random_number % 2 == 0)
        print(f'Question: {random_number}')
        user_answer = input('Your answer: ')
        correct_answer = 'yes' if is_number_even else 'no'

        if user_answer == correct_answer:
            print('Correct!')
        else:
            return print(f'{user_answer} is wrong answer ;(. Correct answer was {correct_answer}\n'
                         f"Let's try again, {name}!")

    return print(f'Congratulations, {name}!')