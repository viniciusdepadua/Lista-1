import sys
import math

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


def is_prime(number):
    """Check if a number is a prime number"""

    prime = True
    for i in range(2, math.floor(math.sqrt(number) + 1)):
        if number % i == 0:
            prime = False
            break
    return prime


def test_is_prime():
    """Test if function is doing ok with some test case"""

    test(is_prime(11))
    test(not is_prime(35))
    test(is_prime(19911121))


test_is_prime()