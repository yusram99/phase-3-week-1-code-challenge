import pytest
from test.challenge1.challenge1 import convert_to_24_hour_format

def test_convert_to_24_hour_format():
    assert convert_to_24_hour_format(8, 30, "am") == "0830"
    assert convert_to_24_hour_format(8, 30, "pm") == "2030"
    assert convert_to_24_hour_format(12, 15, "am") == "0015"
    assert convert_to_24_hour_format(12, 15, "pm") == "1215"


