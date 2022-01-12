"""docstring for cli file."""
import prompt


def welcome_user():
    """Welcome user func. Returns user name"""
    name = prompt.string('May I have your name? ')
    print('Hello,', name, '!')

    return name
