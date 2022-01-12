"""Blank template for every game."""
from brain_games.cli import name


def template_game(func):
    """
    Realise logic for game. Gain func with game logic.
    Returns True if user wins 3 times.
    """
    # name = welcome_user()
    win_game = 0

    while win_game != 3:

        answer, right_answer = func()

        if answer == right_answer:
            win_game += 1
            print('Correct!')
        else:
            print("'%s' is wrong answer ;(. Correct answer was '%s'."
                  % (answer, right_answer))
            print("Let's try again, %s!" % name)
            return False

    print('Congratulations, %s!' % name)
    return True
