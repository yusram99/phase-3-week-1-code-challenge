import pytest
from challenge2 import exactly_two_positive

def test_exactly_two_positive():
    assert exactly_two_positive(2, 4, -3) == True
    assert exactly_two_positive(-4, 6, 8) == True
    assert exactly_two_positive(4, -6, 9) == True
    assert exactly_two_positive(-4, 6, 0) == False
    assert exactly_two_positive(4, 6, 10) == False
    assert exactly_two_positive(-14, -3, -4) == False


