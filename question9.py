import sys


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


def is_palindrome(string):
    """A function that recognizes palindromes"""

    palindrome = False
    if string == string[len(string)::-1]:
        palindrome = True
    return palindrome


def test_is_palindrome():
    """Some test cases to see if the function is doing alright"""

    test(is_palindrome("abba"))
    test(not is_palindrome("abab"))
    test(is_palindrome("tenet"))
    test(not is_palindrome("banana"))
    test(is_palindrome("straw warts"))
    test(is_palindrome("a"))


test_is_palindrome()