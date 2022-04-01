import pytest
from ..src.kmh_to_ms import *

def test_kmh_to_ms():
    velocity_kmh = 120
    expected_output = 33.333
    obtained_output = kmh_to_ms(velocity_kmh)
    assert expected_output == obtained_output
