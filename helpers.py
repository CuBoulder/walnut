"""Walnut Helper Functions."""
from random import choice
from string import ascii_lowercase


def randomstring(length=14):
    """Return a random string of lowercase characters."""
    random_string = ''.join(choice(ascii_lowercase) for i in range(length))
    return random_string
