import pytest
from dsa.data_structures.stacks_and_queue.stacks_and_queue import Node, Linked_list, Queue, Stack


def test_ll():
    assert Linked_list()

def test_node():
    assert Node("test")

# Stack tests
def test_stack():
    assert Stack()

def test_stack_push():
    number_stack = Stack()
    number_stack.push(1)
    actual = number_stack.peek()
    expected = 1
    assert actual == expected

def test_stack_push_two():
    number_stack = Stack()
    number_stack.push(1)
    number_stack.push(2)
    actual = number_stack.peek()
    expected = 2
    assert actual == expected

def test_stack_pop():
    number_stack = Stack()
    number_stack.push(1)
    number_stack.push(2)
    actual = number_stack.pop()
    expected = 2
    assert actual == expected

# Queue tests
def test_queue_empty():
    colors = Queue()
    actual = colors.is_empty()
    expected = True

def test_enqueue():
    colors = Queue()
    colors.enqueue('red')
    colors.enqueue('orange')
    actual = colors.peek()
    expected = 'orange'

def test_dequeue():
    colors = Queue()
    colors.enqueue('red')
    actual = colors.dequeue()
    expected = 'red'
    assert actual == expected





