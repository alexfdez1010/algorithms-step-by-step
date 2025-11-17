from random import choice
from string import ascii_lowercase


def generate_word(length):
    """
    Generates a random word of the given length.
    :param length: length of the word
    :return: a random word of the given length
    """
    return "".join(choice(ascii_lowercase) for _ in range(length))


def generate_two_words(n: int, m: int) -> str:
    """
    Generates two random words of the given length.
    :param n: length of the first word
    :param m: length of the second word
    :return: two random words of the given length
    """
    return f"{generate_word(n)}\n{generate_word(m)}\n"


def generate_dna_sequence(length: int) -> str:
    """
    Generates a random DNA sequence of the given length.
    :param length: length of the DNA sequence
    :return: a random DNA sequence containing A, C, G, T
    """
    nucleotides = ["A", "C", "G", "T"]
    return "".join(choice(nucleotides) for _ in range(length))


def generate_two_dna_sequences(n: int, m: int) -> str:
    """
    Generates two random DNA sequences of the given lengths.
    :param n: length of the first DNA sequence
    :param m: length of the second DNA sequence
    :return: two random DNA sequences separated by newline
    """
    return f"{generate_dna_sequence(n)}\n{generate_dna_sequence(m)}\n"
