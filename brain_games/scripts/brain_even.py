"""Play in Even-game"""
import random


def even_game(name=''):
    """Realise logic for game"""
    win_game = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')

    while win_game != 3:
    
        number = random.randint(1, 100) 
        right_answer = 'yes' if number % 2 == 0 else 'no'
        answer = ''
    
        while answer not in ['yes','no','Yes','No']:
            print('Question: ', number)
            answer = input("Your answer: ",)
        
        # win_game += 1 if answer == right_answer else 0
        if answer == right_answer:
            win_game += 1
            print('Correct!')
        else:
            win_game = 0
            print("'%s' is wrong answer ;(. Correct answer was '%s'." %
                (answer, right_answer))
            
    if win_game == 3:
        print('Congratulations, ', name)
                    
    
# even_game()
