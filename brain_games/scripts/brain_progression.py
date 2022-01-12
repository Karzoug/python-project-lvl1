"""Play in Progression-game."""

from .game_template import template_game
from brain_games.scripts.games import main as games_main
import random


def main():

    games_main()
    print('What number is missing in the progression?')

    @template_game
    def progression_logic(answer='', right_answer=''):
        progression_length = random.randint(6, 10)
        number = random.randint(1, 10)
        step_inc = random.randint(2, 10)
        missing_pos = random.randint(1, progression_length)
        progression = []

        for i in range(0, progression_length):
            if i == missing_pos:
                right_answer = number
                progression.append('..')
            else:
                progression.append(number)
            number += step_inc

        print('Question: ', progression)
        answer = input("Your answer: ",)

        return answer, right_answer
