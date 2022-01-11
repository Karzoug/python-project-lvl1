"""Play in GCD-game"""
from .game_template import template_game
from brain_games.scripts.games import main as games_main
import random

def main():
    
    games_main()
    print('Find the greatest common divisor of given numbers.')
    
    @template_game
    def gcd_logic(answer = '', right_answer = ''):
        number1 = random.randint(1,100)
        number2 = random.randint(1,100)

        if number1 < number2:
            # number1 is always bigger than number2
            number1,number2 = number2,number1 
        
        if number1 % number2 == 0:
            gcd = number2
        
        else:
            gcd = number2 // 2
            while number1 % gcd == 0 and number2 % gcd == 0:
                gcd -= 1           
        right_answer = gcd
    
        while not isinstance(answer,int):
            print("Question: ", number1, number2)
            answer = int(input("Your answer: ",))
        
        return answer, right_answer


