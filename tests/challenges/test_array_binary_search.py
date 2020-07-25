from dsa.challenges.array_binary_search.array_binary_search import binary_search


def test_binary_search_negative():
    actual = binary_search([1, 2, 3, 4, 5], -2)
    expected = -1
    assert actual == expected


# def test_binary_search_zero():
#     actual = binary_search([1, 2, 3, 4, 5], 0)
#     expected = 1
#     assert actual == expected


# def test_binary_search_two():
#     actual = binary_search([1, 2, 3, 4, 5], 2)
#     expected = 3
#     assert actual == expected


def test_binary_search_seven():
    actual = binary_search([15, 16, 17, 18, 19, 20], 7)
    expected = -1
    assert actual == expected
