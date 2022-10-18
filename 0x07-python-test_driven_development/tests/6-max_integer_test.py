#!/usr/bin/python3

import unittest
import sys
sys.path.append('../')

max_integer = __import__('6-max_integer').max_integer

"""This module is for unit testing of the max_integer function"""


class TestMaxInteger(unittest.Testcase):
    def test_ints(self):
        """asserts whether returned value is theright one"""
        self.assertEqual(max_integer([1, 2, 4, 5]), 5)
        self.assertEqual(max_intger([34, 10, 0]), 34)
        self.assertEqual(max_integer([78, 90, 45, 16]), 90)

    def test_duplicates(self):
        """asserts whether returns correct value even with duplicates"""
        self.assertEqual(max_integer([1, 2, 16, 16, 56]), 56)
        self.assertEqual(max_integer([4, 4, 5, 7, 9, 9]), 9)
        self.assertEqual(max_integer([2, 2]), 2)

    def test_element(self):
        """tests when there is only 1 element in list"""
        self.assertEqual(maxt_integer([1]), 1)
        self.assertEqual(max_intger([5]), 5)
