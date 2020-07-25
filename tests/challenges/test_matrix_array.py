from dsa.challenges.matrix_array.matrix_array import matrix_array


def test_matrix_array_two():
    actual = matrix_array([[1, 2, 3], [4, 5, 6]])
    expected = [6, 15]
    assert actual == expected


def test_matrix_array_four():
    actual = matrix_array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    expected = [6, 15, 24, 33]
    assert actual == expected


def test_matrix_array_two_five():
    actual = matrix_array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    expected = [15, 40]
    assert actual == expected
