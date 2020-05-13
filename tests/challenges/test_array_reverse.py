from dsa.challenges.array_reverse.array_reverse import array_reverse

def test_array_reverse_five():
  actual = array_reverse([1, 2, 3, 4, 5])
  expected = [5, 4, 3, 2, 1]
  assert actual == expected

def test_array_reverse_ten():
  actual = array_reverse([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
  expected = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
  assert actual == expected