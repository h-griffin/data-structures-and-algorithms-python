import pytest
from dsa.challenges.queue_with_stacks.queue_with_stacks import PseudoQueue

def test_enqueue_two():
    pq = PseudoQueue()
    pq.enqueue('apples')
    pq.enqueue('bananas')

    actual = pq.dequeue()
    expected = 'apples'
    assert actual == expected

    actual = pq.dequeue()
    expected = 'bananas'
    assert actual == expected

def test_en_de_en_de():
    pq = PseudoQueue()
    pq.enqueue('apples')
    pq.enqueue('bananas')

    pq.dequeue

    pq.enqueue('carrots')
    pq.enqueue('donuts')

    actual = [pq.dequeue(), pq.dequeue(), pq.dequeue()]
    expected = ['bananas', 'carrots', 'donuts']
    assert actual == expected


def test_dequeue_empty():
    pq = PseudoQueue()
    with pytest.raises(RuntimeError):
        pq.dequeue()

