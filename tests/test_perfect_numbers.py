import pytest
from ..src.perfect_numbers import *  # noqa

def test_divide_number():
    dividend = 6
    divisor = 2
    expected_output = 3
    obtained_output = divide_number(dividend,divisor)
    assert expected_output == obtained_output

def test_get_perfect_numbers():
    starting_number = 1
    finishing_number = 30
    expected_output = [6,28]
    obtained_output = get_perfect_numbers(starting_number,finishing_number)
    assert expected_output == obtained_output
