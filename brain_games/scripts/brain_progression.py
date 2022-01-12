"""Play in Progression-game."""

from .game_template import template_game
import random


def main():

    print('What number is missing in the progression?')

    @template_game
    def progression_logic(answer='', right_answer=''):
        progression_length = random.randint(6, 10)
        number = random.randint(1, 10)
        step_inc = random.randint(2, 10)
        missing_pos = random.randint(1, progression_length)
        right_answer = number + step_inc * (missing_pos - 1)

        print('Question:', end=" ")

        for i in range(1, progression_length + 1):

            print("..", end=" ") if i == missing_pos else print(number, end=" ")
            number += step_inc

        answer = input("\nYour answer: ",)

        return answer, right_answer
