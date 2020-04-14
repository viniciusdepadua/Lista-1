import sys


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


def complex_sum(z, w):
    """ Representing a complex number as a tuple of
    two numeric values, and creating a function
    that calculates the addition of two of them """

    sum_complex = (z[0] + w[0], z[1] + w[1])
    return sum_complex


def test_complex_sum():
    test(complex_sum((1, 2),(2, 3)) == (3, 5))


test_complex_sum()
