def binary_search(arr ,key):
  if key < len(arr) and key >= 0:
    return arr[key]
  elif key >= len(arr) or key < 0:
    return -1