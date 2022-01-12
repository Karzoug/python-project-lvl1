"""Play in Even-game"""
from .game_template import template_game
from brain_games.scripts.games import main as games_main
import random


def main():

    games_main()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    @template_game
    def even_logic(answer='', right_answer=''):
        number = random.randint(1, 100)
        right_answer = 'yes' if number % 2 == 0 else 'no'

        while answer not in ['yes', 'no', 'Yes', 'No']:
            print('Question:', number)
            answer = input("Your answer: ",)

        return answer, right_answer
