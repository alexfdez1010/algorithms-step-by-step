from typing import List


def latex_wrapper(function):
    """
    Decorator to wrap a function that returns a string in LaTeX format.
    :param function: The function to wrap.
    """

    def wrapper(*args, **kwargs):
        return f"$\n{function(*args, **kwargs)}\n$"

    return wrapper


def latex_to_markdown(latex_string) -> str:
    """
    Convert a LaTeX string to Markdown format.
    :param latex_string: The LaTeX string to convert.
    :return: The Markdown string.
    """
    return f"$$\n{latex_string}\n$$"


def matrix_to_markdown(matrix: List[List[float]]) -> str:
    """
    Convert a matrix to Markdown format.
    :param matrix: The matrix to convert.
    """
    markdown = "\\begin{pmatrix}\n"

    for row in matrix:
        markdown += " & ".join([str(x) if x != float('inf') else "\\infty" for x in row]) + "\\\\\n"

    markdown += "\\end{pmatrix}\n"
    return markdown


def matrix_multiplication_to_markdown(matrix1: List[List[float]],
                                      matrix2: List[List[float]],
                                      result: List[List[float]]) -> str:
    """
    Convert a matrix multiplication to Markdown format.
    :param matrix1: The first matrix.
    :param matrix2: The second matrix.
    :param result: The result of the multiplication.
    """
    markdown = matrix_to_markdown(matrix1)
    markdown += "\\times\n"
    markdown += matrix_to_markdown(matrix2)
    markdown += "= \n"
    markdown += matrix_to_markdown(result)
    return markdown
