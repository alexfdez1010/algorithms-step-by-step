from typing import Tuple, Optional


def only_one_parameter_positive_number(input_string) -> Tuple[bool, Optional[str]]:
    """
    Checks if the input string has only one parameter
    :param input_string: The input string
    :return: True if the input string has only one parameter, False otherwise
    """
    lines = input_string.splitlines()
    if len(lines) != 1:
        return False, "The input string must contain only one line"

    line = lines[0]
    line = line.split()

    if len(line) != 1:
        return False, "The input string must contain only one parameter"

    try:
        n = int(line[0])
    except ValueError:
        return False, "The input string must contain only one integer parameter"

    if n <= 0:
        return False, "The input string must contain only one positive integer parameter"

    return True, None


def two_strings(input_string) -> Tuple[bool, Optional[str]]:
    """
    Checks if the input string has two strings
    :param input_string: The input string
    :return: True if the input string has two strings, False otherwise
    """
    lines = input_string.splitlines()
    if len(lines) != 2:
        return False, "The input string must contain two lines"

    for line in lines:
        line = line.split()
        if len(line) != 1:
            return False, "The input string must contain two strings"

    return True, None
