#!/usr/bin/python3
""" module to test ``6-max_integer`` module using unittest"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """ Defines a class TestMaxInteger for testing max_integer() function """

    def test_MaxInteger(self):
        """ tests the maximun integer """
        self.assertIsNone(max_integer([]))
        self.assertEqual(max_integer([9]), 9)
        self.assertEqual(max_integer([-1, 9]), 9)
        self.assertEqual(max_integer([2, 4, 56, 566]), 566)
