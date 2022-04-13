import pytest
from ..src.perfect_numbers import *  # noqa

def test_sum_its_divisors():
    number=10
    expected_output = 8
    obtained_output = sum_its_divisors(number)
    assert expected_output == obtained_output

def test_get_perfect_numbers():
    starting_number = 1
    finishing_number = 30
    expected_output = [6,28]
    obtained_output = get_perfect_numbers(starting_number,finishing_number)
    assert expected_output == obtained_output
    