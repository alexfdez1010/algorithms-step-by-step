from random import choice
from string import ascii_lowercase


def generate_word(length):
    """
    Generates a random word of the given length.
    :param length: length of the word
    :return: a random word of the given length
    """
    return ''.join(choice(ascii_lowercase) for _ in range(length))


def generate_two_words(n: int, m: int) -> str:
    """
    Generates two random words of the given length.
    :param n: length of the first word
    :param m: length of the second word
    :return: two random words of the given length
    """
    return f"{generate_word(n)}\n{generate_word(m)}\n"
