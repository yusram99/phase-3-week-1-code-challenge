import pytest
from challenge3 import solve

def test_solve():
    assert solve("zodiacs") == 26
    assert solve("strength") == 57
