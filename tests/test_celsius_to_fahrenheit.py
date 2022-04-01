import pytest
from ..src.celsius_to_fahrenheit import convert_celsius_to_fahrenheit

def test_convert_celsius_to_fahrenheit():
    degrees_celsius=4
    expected_output = 39.2
    obtained_temperature = convert_celsius_to_fahrenheit(degrees_celsius)
    assert expected_output == obtained_temperature
