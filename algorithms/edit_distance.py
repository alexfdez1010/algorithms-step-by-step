from utils.markdown_utils import markdown_table


def edit_distance(input_string: str) -> str:
    """
    Computes the edit distance between two strings.
    """
    lines = input_string.splitlines()
    string1 = lines[0]
    string2 = lines[1]
    n = len(string1)
    m = len(string2)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    headers_rows = ["$"] + list(string2)
    headers_columns = ["$"] + list(string1)

    for i in range(n + 1):
        dp[i][0] = i

    for j in range(m + 1):
        dp[0][j] = j

    yield "The table have been filled with the base cases " \
          "that are the edit distance between an empty string and a non-empty string."
    yield "Note: '$' Represents the empty string."
    yield markdown_table(dp, headers_rows, headers_columns)

    yield "Having filled the table with the base cases, we can now fill the rest of the table."

    for i in range(1, n + 1):
        yield f"### Step {i}"
        for j in range(1, m + 1):
            if string1[i - 1] == string2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

        yield markdown_table(dp, headers_rows, headers_columns)

    yield f"The final table is:"
    yield markdown_table(dp, headers_rows, headers_columns)
    yield f"The edit distance between {string1} and {string2} is {dp[n][m]}."
