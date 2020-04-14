import sys


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


def sum_of_squares(xs):
    """Computes the sum of the squares of the
numbers in the list xs."""

    sum_squares = 0
    for number in xs:
        sum_squares += number * number
    return sum_squares


def test_sum_of_squares():
    """Some test cases to see if the function is doing alright"""

    test(sum_of_squares([2, 3, 4]) == 29)
    test(sum_of_squares([]) == 0)
    test(sum_of_squares([2, -3, 4]) == 29)


test_sum_of_squares()