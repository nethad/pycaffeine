__author__ = 'thomas'

import unittest
from pycaffeine import CafDeque

class TestCafDeque(unittest.TestCase):

    def setUp(self):
        pass
        self.deque = CafDeque()

    def test_deque_is_empty(self):
        self.assertTrue(self.deque.is_empty())

    def test_deque_has_zero_length(self):
        self.assertEqual(self.deque.length(), 0)

    def test_push_one_item(self):
        self.deque.push("first")
        self.assertFalse(self.deque.is_empty())
        self.assertEqual(self.deque.length(), 1)

    def test_pop_one_item(self):
        self.deque.push("first")
        value = self.deque.pop()
        self.assertEqual(value, "first")

if __name__ == '__main__':
    unittest.main()
