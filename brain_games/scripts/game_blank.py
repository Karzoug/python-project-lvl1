"""Blank for every game"""
import random
from brain_games.cli import welcome_user


def blank_game(game_name=''):
    """Realise logic for game"""
    win_game = 0
    name = welcome_user()

    while win_game != 3:
        answer = ""
        right_answer = ""
    
        if game_name == 'game_even':
            number = random.randint(1, 100) 
            right_answer = 'yes' if number % 2 == 0 else 'no'
        
            while answer not in ['yes','no','Yes','No']:
                print('Question: ', number)
                answer = input("Your answer: ",)

        elif game_name == 'game_calc':
            number1 = random.randint(1,50)
            number2 = random.randint(1,50)
            operand = random.choice(['+','-','*'])

            if operand == '+':
                right_answer = number1 + number2
            elif operand == '-':
                right_answer = number1 - number2
            else:
                right_answer = number1 * number2
            
            while not isinstance(answer,int):
                print("Question: ", number1, operand, number2)
                answer = int(input("Your answer: ",))

        elif game_name == 'game_gcd':
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

        else:
            print('Wrong game name!')
            break

        # win_game += 1 if answer == right_answer else 0
        if answer == right_answer:
            win_game += 1
            print('Correct!')
        else:
            win_game = 0
            print("'%s' is wrong answer ;(. Correct answer was '%s'." %
                (answer, right_answer))

            if game_name == 'game_calc':
                print("Let's try again, ", name)
                break
            
    if win_game == 3:
        print('Congratulations, ', name)
                    
    
# even_game()
