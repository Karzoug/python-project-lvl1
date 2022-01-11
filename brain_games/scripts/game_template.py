"""Blank template for every game"""
from brain_games.cli import welcome_user


def template_game(func):
    """Realise logic for game"""
    name = welcome_user()
    win_game = 0
    
    while win_game != 3:

        answer, right_answer = func()

        if answer == right_answer:
            win_game +=1
            print('Correct!')
        else:
            print("'%s' is wrong answer ;(. Correct answer was '%s'." %
                 (answer, right_answer))
            print("Let's try again, %s!" %name)
            return False

    print("Congratulations, %s!" %name)
    return True
