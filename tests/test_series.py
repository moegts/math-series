## importing ##

from math_series import __version__
from math_series.series import fibonacci, lucas, sum_series

## test version ##


def test_version():
    assert __version__ == '0.1.0'

## Testing Fibancci ##


def test_fibonacci_0():
    excepted, actual = 0, fibonacci(0)
    assert excepted == actual


def test_fibonacci_1():
    excepted, actual = 1, fibonacci(1)
    assert excepted == actual


def test_fibonacci_2():
    excepted, actual = 1, fibonacci(2)
    assert excepted == actual


def test_fibonacci_3():
    excepted, actual = 2, fibonacci(3)
    assert excepted == actual

## Testing Lucas ##


def test_lucas_0():
    excepted, actual = 2, lucas(0)
    assert excepted == actual


def test_lucas_1():
    excepted, actual = 1, lucas(1)
    assert excepted == actual


def test_lucas_2():
    excepted, actual = 3, lucas(2)
    assert excepted == actual


def test_lucas_3():
    excepted, actual = 4, lucas(3)
    assert excepted == actual


## Testing sum_series ##

def test_sum_series_0():
    excepted, actual = 1, sum_series(1)
    assert excepted == actual


def test_sum_series_1():
    excepted, actual = 1, sum_series(2)
    assert excepted == actual


def test_sum_series_2():
    excepted, actual = 9, sum_series(3, 3, 3)
    assert excepted == actual


def test_sum_series_3():
    excepted, actual = 20, sum_series(4, 4, 4)
    assert excepted == actual
