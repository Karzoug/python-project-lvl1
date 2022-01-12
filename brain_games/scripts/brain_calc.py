"""Play in Calc-game"""
from .game_template import template_game
from brain_games.scripts.games import main as games_main
import random


def main():

    games_main()
    print('What is the result of the expression?')

    @template_game
    def calc_logic(answer='', right_answer=''):
        number1 = random.randint(1, 50)
        number2 = random.randint(1, 50)
        operand = random.choice(['+', '-', '*'])

        if operand == '+':
            right_answer = number1 + number2
        elif operand == '-':
            right_answer = number1 - number2
        else:
            right_answer = number1 * number2

        while not isinstance(answer, int):
            print("Question: ", number1, operand, number2)
            answer = int(input("Your answer: ",))

        return answer, right_answer
