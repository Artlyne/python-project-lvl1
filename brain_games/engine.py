from brain_games.cli import welcome_user


def game_core(game_module):
    game_task = game_module.game_task
    print(f'Welcome to the Brain Games!\n{game_task}\n')
    name = welcome_user()[0]

    for game_round in range(3):
        question, correct_answer = game_module.ask()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')

        if user_answer == str(correct_answer):
            print('Correct!')
        else:
            return print(f'{user_answer} is wrong answer ;(. '
                         f'Correct answer was {correct_answer}.\n'
                         f"Let's try again, {name}!")
    return print(f'Congratulations, {name}!')
