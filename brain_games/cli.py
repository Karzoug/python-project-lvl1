#!/usr/bin/python3

"""docstring for cli file."""
import prompt


def welcome_user():
    """Welcome user func."""
    name = prompt.string('May I have your name? ')
    print('Hello,', name, '!')
