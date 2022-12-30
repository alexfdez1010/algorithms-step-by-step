from typing import List, Optional, Any


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


def markdown_table(data: List[List[Any]],
                   headers_row: Optional[List[str]] = None,
                   headers_column: Optional[List[str]] = None) -> str:
    """
    Convert a list of lists to a Markdown table.
    :param data: The data to convert.
    :param headers_row: The headers for the rows.
    :param headers_column: The headers for the columns.
    """

    if not isinstance(data[0][0], str):
        data = [[str(x) for x in row] for row in data]

    rows = []

    if headers_column:
        headers_row = [""] + headers_row

    if headers_row:
        rows.append("| " + " | ".join(headers_row) + " |")
        rows.append("| " + " | ".join([":---:"] * len(headers_row)) + " |")

    for row in data:
        rows.append("| " + " | ".join(row) + " |")

    if headers_column:
        for i, row in enumerate(rows[2:], 2):
            rows[i] = f"| **{headers_column[i - 2]}** {row}"

    return "\n".join(rows)
