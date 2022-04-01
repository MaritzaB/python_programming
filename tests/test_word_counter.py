import pytest
from ..src.word_counter import *

def test_word_counter():
    quote = "Hola mundo"
    expected_output = 2
    obtained_output = word_counter(quote)
    assert expected_output == obtained_output
