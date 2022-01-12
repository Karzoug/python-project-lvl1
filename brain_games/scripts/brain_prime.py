"""Play in Prime-game"""
from .game_template import template_game
from brain_games.scripts.games import main as games_main
import random


def main():

    games_main()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    @template_game
    def prime_logic(answer='', right_answer=''):
        number = random.randint(1, 100)
        dividers = [b for b in range(2, number // 2) if number % b == 0]
        right_answer = 'no' if dividers else 'yes'

        while answer not in ['yes', 'no', 'Yes', 'No']:
            print('Question: ', number)
            answer = input("Your answer: ")

        return answer, right_answer
