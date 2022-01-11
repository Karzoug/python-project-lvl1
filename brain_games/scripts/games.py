"""Execute main module."""
from brain_games.cli import welcome_user
import brain_even

def main():
    """Execute main function body."""
    print('Welcome to the Brain Games!')    
    name = welcome_user()
    brain_even()

if __name__ == '__main__':

    main()
