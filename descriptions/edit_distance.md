Edit distance is a measure of the similarity between two strings. It represents the minimum number of operations (
insertions, deletions, or substitutions) needed to transform one string into the other.

One way to calculate the edit distance between two strings is to use dynamic programming. Dynamic programming is a
technique for solving problems by breaking them down into smaller subproblems, solving each subproblem, and storing the
solution to each subproblem so that it can be reused later.

To calculate the edit distance between two strings using dynamic programming, we can use the following steps:

1. Define a matrix to store the solutions to each subproblem. The matrix should have the same number of rows as the
   length of the first string and the same number of columns as the length of the second string.

2. Initialize the first row and first column of the matrix to represent the cost of transforming an empty string into
   the first string or the second string, respectively. The cost of transforming an empty string into a non-empty string
   is equal to the length of the non-empty string (since we need to insert all characters in the non-empty string).

3. Iterate over the remaining cells of the matrix and fill in the matrix using the following formula (where x is 0 if
   the characters at positions i-1 and j-1 in the two strings are the same, and 1 if they are different):

```text
matrix[i][j] = min(matrix[i-1][j] + 1,   # insertion
                   matrix[i][j-1] + 1,   # deletion
                   matrix[i-1][j-1] + x)  # substitution
```

4. The edit distance between the two strings is the value in the bottom-right cell of the matrix.