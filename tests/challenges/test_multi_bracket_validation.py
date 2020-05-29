
from dsa.challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation

def test_multi_bracket_validation_true():
    actual = multi_bracket_validation('()[]')
    expected = True
    assert actual == expected

def test_multi_bracket_validation_false():
    actual = multi_bracket_validation('(])')
    expected = False
    assert actual == expected

