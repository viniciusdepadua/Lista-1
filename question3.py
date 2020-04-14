import sys


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


def sum_to(n):
    """returns the sum of all integer numbers up
to and including n."""

    sum_value = 0
    for i in range(1, n + 1):
        sum_value = sum_value + i
    return sum_value


def test_sum_to():
    """Some tests cases to sse if the function is doing alright"""

    test(sum_to(100) == 5050)
    test(sum_to(10000) == 50005000)


test_sum_to()
