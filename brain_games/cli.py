"""docstring for cli file."""


def welcome_user():
    """Welcome user func. Returns user name"""
    name = input('May I have your name? ')
    print('Hello,', name, '!')

    return name
