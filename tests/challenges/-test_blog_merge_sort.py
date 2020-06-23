from dsa.challenges.blog_merge_sort.blog_merge_sort import merge_sort


def test_merge_sort():
    actual = merge_sort([4, 3, 5, 2, 1])
    expected = [1, 2, 3, 4, 5]
    assert actual == expected

def test_merge_sort_given():
    actual = merge_sort([8, 4, 23, 42, 16, 15])
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected

def test_merge_sort_nagatives():
    actual = merge_sort([-8, -4, -23, -42, -16, -15])
    expected = [-42, -23, -16, -15, -8, -4]
    assert actual == expected

