import pytest
from dsa.challenges.queue_with_stacks.queue_with_stacks import PseudoQueue, Node, Stack


def test_node():
    assert Node("test")

def test_stack():
    assert Stack()

def test_PseudoQueue():
    assert PseudoQueue()

# def test_pq_en_2():
#     pq = PseudoQueue()
#     pq.enqueue('apples')
#     pq.enqueue('bananas')
#     actual = str(pq._inbox)
#     expected = "[bananas] -> [apples] -> NULL"
#     assert actual == expected

# def test_PseudoQueue_enqueue_multiple_items():
#     my_queue = PseudoQueue()
#     my_queue.enqueue(1)
#     my_queue.enqueue(2)
#     my_queue.enqueue(3)
#     actual = str(my_queue._inbox)
#     expected = "[3] -> [2] -> [1] -> NULL"
#     assert actual == expected


# def test_enqueue_two():
#     pq = PseudoQueue()
#     pq.enqueue('apples')
#     pq.enqueue('bananas')

#     actual = pq.dequeue()
#     expected = 'apples'
#     assert actual == expected

#     actual = pq.dequeue()
#     expected = 'bananas'
#     assert actual == expected

# def test_en_de_en_de():
#     pq = PseudoQueue()
#     pq.enqueue('apples')
#     pq.enqueue('bananas')

#     pq.dequeue()

#     pq.enqueue('carrots')
#     pq.enqueue('donuts')

#     actual = [pq.dequeue(), pq.dequeue(), pq.dequeue()]
#     expected = ['bananas', 'carrots', 'donuts']
#     assert actual == expected


def test_dequeue_empty():
    pq = PseudoQueue()
    with pytest.raises(RuntimeError):
        pq.dequeue()

