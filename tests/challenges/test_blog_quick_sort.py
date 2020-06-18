from dsa.challenges.blog_quick_sort.blog_quick_sort import quick_sort


def test_sample_array():
    alist = [8,4,23,42,16,15]
    left = 0
    right = len(alist) - 1
    quick_sort(alist, left, right)
    expected = [4, 8, 15, 16, 23, 42]
    assert alist == expected

def test_simple_array():
    alist = [4,3,5,2,1]
    left = 0
    right = len(alist) - 1
    quick_sort(alist, left, right)
    expected = [1,2,3,4,5]
    assert alist == expected

def test_negative_array():
    alist = [-3, -2, -5, -1, -4]
    left = 0
    right = len(alist) - 1
    quick_sort(alist, left, right)
    expected = [-5, -4, -3, -2, -1]
    assert alist == expected
