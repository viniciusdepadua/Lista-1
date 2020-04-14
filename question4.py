import sys


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


def sum_list(list_data):
    """Sums all the elements in a list up to
but not including the first even number."""

    sum_value = 0
    for number in list_data:
        if number % 2 == 1:
            sum_value += number
        else:
            break
    return sum_value


def test_sum_list():
    """Some test cases to sse if the function is doing alright """

    test(sum_list([1, 5, 7, 3, 4, 5, 7, 9, 12]) == 16)
    test(sum_list([3, 3, 3, 3, 3, 3, 3]) == 21)
    test(sum_list([2, 2, 2, 2]) == 0)


test_sum_list()
