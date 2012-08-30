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
        self.assertEqual(len(self.deque), 0)

    def test_push_one_item(self):
        self.deque.push("first")
        self.assertFalse(self.deque.is_empty())
        self.assertEqual(len(self.deque), 1)

    def test_pop_one_item(self):
        self.deque.push("first")
        value = self.deque.pop()
        self.assertEqual(value, "first")

    def test_contains_false(self):
        self.deque.push("inqueue")
        self.deque.push("inqueue1")
        self.deque.push("inqueue2")
        in_queue = self.deque.__contains__("notinqueue")
        self.assertFalse(in_queue)

    def test_contains_true(self):
        self.deque.push("inqueue")
        self.deque.push("inqueue1")
        self.deque.push("inqueue2")
        self.assertTrue(self.deque.__contains__("inqueue"))
        self.assertTrue(self.deque.__contains__("inqueue1"))
        self.assertTrue(self.deque.__contains__("inqueue2"))

    def test_getitem(self):
        self.deque.push("value1")
        self.assertEqual(self.deque[0], "value1")

    def test_getitem_indexerror(self):
        self.deque.push("value1")
        self.assertRaises(IndexError, self.deque.__getitem__, 1)

    def test_setitem(self):
        self.deque.push("value1")
        self.deque[0] = "value2"
        self.assertEqual(len(self.deque), 1)
        self.assertEqual(self.deque[0], "value2")

if __name__ == '__main__':
    unittest.main()
