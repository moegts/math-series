#### fibonacci function ####

"""
    fibonacci do sum serise of first value 0 for n = 0 and n = 1 and
    by implimenting function using : recursion.
"""


def fibonacci(n):
    if n <= 1: return n
    else: return(fibonacci(n-1) + fibonacci(n-2))

#### lucas function ####


"""
lucas do sum serise with the first value of 2 for n = 0 and 1 for n = 1
by implimenting function using : recursion.
"""


def lucas(n):
    if n == 0: return 2
    elif n == 1: return 1
    return lucas(n - 1) + lucas(n - 2)

#### sum_series function ####


"""
cheack if the  input  fibonacci or lucas or the sum of both
n to make a the serise
n1 the base case for index 0
n2 the base case for index 1
"""


def sum_series(n, n1=0, n2=1):
    if n == 0: return n1
    elif n==1: return n2
    return sum_series(n-1, n1, n2) + sum_series(n-2, n1, n2)