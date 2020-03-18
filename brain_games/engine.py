from brain_games.cli import welcome_user


def run(game_module):
    game_task = game_module.GAME_TASK
    print(f'Welcome to the Brain Games!\n{game_task}\n')
    name = welcome_user()

    rounds = 3
    for _ in range(rounds):
        question, correct_answer = game_module.generate_round()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')

        if user_answer == str(correct_answer):
            print('Correct!')
        else:
            return print(f'{user_answer} is wrong answer ;(. '
                         f'Correct answer was {correct_answer}.\n'
                         f"Let's try again, {name}!")
    return print(f'Congratulations, {name}!')
