The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. The terms of the Fibonacci sequence are defined by the following recurrence relation:

F(n) = F(n-1) + F(n-2)

with the initial conditions:

F(0) = 0
F(1) = 1

One way to calculate the n-th term of the Fibonacci sequence is to use matrix exponentiation. We can define a matrix A as follows:

A = [1, 1]
[1, 0]

Now, we can express the recurrence relation as a matrix multiplication:

[F(n), F(n-1)] = [F(n-1), F(n-2)] * A

We can use this equation to calculate the n-th term of the Fibonacci sequence by starting with the initial conditions and repeatedly multiplying the matrix A. For example, to calculate F(2), we can start with the initial conditions:

[F(1), F(0)] = [1, 0]

and multiply by A:

[F(2), F(1)] = [F(1), F(0)] * A = [1, 0] * [1, 1]
[1, 0]
= [1, 1]

Thus, F(2) = 1.

To calculate F(3), we can start with the initial conditions and multiply by A again:

[F(3), F(2)] = [F(2), F(1)] * A = [1, 1] * [1, 1]
[1, 0]
= [2, 1]

Thus, F(3) = 2.

We can continue this process to calculate the n-th term of the Fibonacci sequence for any value of n.

Note that this method is much faster than the traditional recursive method for calculating the Fibonacci sequence,
because it only requires O(log n) matrix multiplications instead of O(n) recursive calls.

The input must be a single integer n in only one line.