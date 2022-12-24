from typing import List, Tuple

from utils.markdown_utils import matrix_to_markdown, matrix_multiplication_to_markdown, latex_to_markdown


def fibonacci(input_string):
    """
    Calculates the nth fibonacci number using matrix exponentiation
    """
    n = int(input_string)

    if n == 0:
        return 0

    matrix = [[1, 1], [1, 0]]

    result, markdown_list = __matrix_exponentiation(matrix, n - 1)

    for markdown in markdown_list:
        yield markdown

    yield latex_to_markdown(matrix_to_markdown(result))
    yield f"The {n}th fibonacci is the number located in the top left of the matrix, thus the result is {result[0][0]}"


def __matrix_exponentiation(matrix: List[List[float]], n: int) -> Tuple[List[List[float]], List[str]]:
    """
    Calculates the nth power of a matrix
    :param matrix: The matrix
    :param n: The power to raise the matrix to
    """
    if n <= 1:
        markdown_list = [
            f"## n = {n}",
            f"We start with the following matrix:\n",
            latex_to_markdown(matrix_to_markdown(matrix))
        ]
        return matrix, markdown_list

    if n & 1:
        temp_matrix, markdown_list = __matrix_exponentiation(matrix, n - 1)
        result = __matrix_multiplication(matrix, temp_matrix)
        markdown_list.append(f"## n = {n}\n")
        markdown_list.append(f"As {n} is odd, we need to decrease it by 1 to get an even number")
        markdown_list.append(f"This can be easily achieved by multiplying the matrix by the original")
        markdown_list.append(latex_to_markdown(matrix_multiplication_to_markdown(matrix, temp_matrix, result)))
        return result, markdown_list

    temp_matrix, markdown_list = __matrix_exponentiation(matrix, n // 2)
    result = __matrix_multiplication(temp_matrix, temp_matrix)
    markdown_list.append(f"## n = {n}\n")
    markdown_list.append(f"As {n} is even, we can get this power by squaring the matrix to the power {n // 2}")
    markdown_list.append(latex_to_markdown(matrix_multiplication_to_markdown(temp_matrix, temp_matrix, result)))
    return result, markdown_list


def __matrix_multiplication(matrix1: List[List[float]], matrix2: List[List[float]]):
    """
    Multiplies two matrices
    :param matrix1: The first matrix
    :param matrix2: The second matrix
    """
    result = [[0 for _ in range(len(matrix1))] for _ in range(len(matrix2[0]))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result
