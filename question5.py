import sys


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


def how_many_words(list_data):
    """Counts how many words occur in a list up to and including
        the first occurrence of the word “sam”."""

    words_number = 0
    for words in list_data:
        words_number += 1
        if words == "sam":
            break
    return words_number


def test_how_many_words():
    """Some test cases to see if the function is doing alright."""

    test(how_many_words(["hi ", "my ", "name ", "is ", "sam", "im", "okay"]) == 5)
    test(how_many_words(["hi ", "my ", "name ", "is ", "vinicius", "im", "okay"]) == 7)
    test(how_many_words([]) == 0)


test_how_many_words()
