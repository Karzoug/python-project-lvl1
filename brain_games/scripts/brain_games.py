"""Execute main module."""
from brain_games.cli import welcome_user
from brain_even import even_game


def main():
    """Execute main function body."""
    print('Welcome to the Brain Games!')
    # name = welcome_user() 
    name = 'fdf'   
    even_game(name)
    

if __name__ == '__main__':

    main()
