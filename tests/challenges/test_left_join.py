from dsa.challenges.left_join.left_join import left_join
import pytest

def test_left_join():
    hashmap1 = {
        'fond' : 'enamored',
        'wrath' : 'anger',
    }

    hashmap2 = {
        'fond' : 'averse',
        'wrath' : 'delight',
    }

    actual = left_join(hashmap1, hashmap2)
    expected = [
        ['fond', 'enamored', 'averse'],
        ['wrath', 'anger', 'delight'],
    ]
    assert actual == expected

#joseph z
def test_left_join_none():
    """Different Variables and positions of them
    """
    hashmap1 = {
        'fond' : 'enamored',
        'food' : 'yummy',
        'diligent' : 'employed',
        'guide' : 'usher',
        'flow' : 'boom',
        'computer' : 'network',
    }

    hashmap2 = {
        'random': 'something',
        'fond' : 'averse',
        'wrath' : 'delight',
        'diligent' : 'idle',
        'guide' : 'follow',
        'flow' : 'jam',
    }

    actual = left_join(hashmap1, hashmap2)
    expected = [
        ['fond', 'enamored', 'averse'],
        ['food', 'yummy', None],
        ['diligent', 'employed', 'idle'],
        ['guide', 'usher', 'follow'],
        ['flow', 'boom', 'jam'],
        ['computer', 'network', None]
    ]

    assert actual == expected

# def test_left_join_none():
#     hashmap1 = {
#         'fond' : 'enamored',
#         'dark' : 'stormy',
#         'flow' : 'boom',
#         'bright' : 'sunny',
#     }

#     hashmap2 = {
#         'ignore': 'skip',
#         'fond' : 'averse',
#         'wrath' : 'delight',
#         'flow' : 'jam',
#     }

#     actual = left_join(hashmap1, hashmap2)
#     expected = [
#         ['fond', 'enamored', 'averse'],
#         ['dark', 'stormy', None],
#         ['diligent', 'employed', 'idle'],
#         ['flow', 'boom', 'jam'],
#         ['bright', 'sunny', None]
#     ]
#     assert actual == expected

