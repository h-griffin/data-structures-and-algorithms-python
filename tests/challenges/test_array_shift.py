from dsa.challenges.array_shift.array_shift import insert_shift_array

def test_insert_shift_array_five():
  actual = insert_shift_array([2, 4, 6, 8], 5)
  expected = [2, 4, 5, 6, 8]
  assert actual == expected
  