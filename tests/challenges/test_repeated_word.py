import pytest
from dsa.challenges.repeated_word.repeated_word import repeat_word

def test_repeat_word():
    test = 'it is dark isnt it'
    actual = repeat_word(test)
    expected = 'it'
    assert actual == expected

def test_repeat_word_punctuation():
    test = 'it. is.. dark! isnt it?'
    actual = repeat_word(test)
    expected = 'it'
    assert actual == expected

def test_repeat_word_caps():
    test = 'IT IS DARK ISNT IT'
    actual = repeat_word(test)
    expected = 'IT'
    assert actual == expected

