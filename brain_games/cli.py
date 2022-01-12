"""docstring for cli file."""


def welcome_user():
    """Welcome user func. Returns user name"""
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print('Hello,', name, '!')

    return name


# if __name__ == 'game_template':
name = welcome_user()
