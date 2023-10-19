#!/usr/bin/python3
""" unittests for the base class """
from unittest import TestCase
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
import sys


class TestRectangleClass(TestCase):
    def test_instantiation(self):
        """ tests instantiation and attributes """
        # Test of Rectangle(10, 2) exists
        output = StringIO()
        sys.stdout = output

        r1 = Rectangle(10, 2)
        print(r1)

        sys.stdout = sys.__stdout__
        print_res = output.getvalue()
        self.assertEqual(print_res, "[Rectangle] (6) 0/0 - 10/2\n")

        # Test of Rectangle(2, 10, 2) exists
        r2 = Rectangle(2, 10, 2)
        output = StringIO()
        sys.stdout = output
        print(r2)
        print_res = output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertEqual(print_res, "[Rectangle] (7) 2/0 - 2/10\n")
        self.assertIsInstance(r2, Base)
        self.assertEqual(r2.id - r1.id, 1)

        # Test of Rectangle(2, 10, 2, 12) exists
        r3 = Rectangle(2, 10, 2, 12)
        output = StringIO()
        sys.stdout = output
        print(r3)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Rectangle] (8) 2/12 - 2/10\n")
        self.assertEqual(r3.id, 8)

        # Test of Rectangle(2, 10, 2, 12) exists
        r4 = Rectangle(2, 10, 2, 12, 19)
        self.assertEqual(r4.id, 19)
        self.assertTrue(issubclass(Rectangle, Base))

    def test_values(self):
        """ ensures exceptions are raised approproately"""
        with self.assertRaises(TypeError):
            Rectangle("10", 12)
        with self.assertRaises(TypeError):
            Rectangle(10, "12")
        with self.assertRaises(TypeError):
            Rectangle(10)
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(ValueError):
            Rectangle(-10, 12)
        with self.assertRaises(ValueError):
            Rectangle(10, -12)
        with self.assertRaises(ValueError):
            Rectangle(0, 20)
        with self.assertRaises(ValueError):
            Rectangle(10, 0)
        with self.assertRaises(ValueError):
            Rectangle(10, 20, 10, -34)
        with self.assertRaises(ValueError):
            Rectangle(10, 20, -10, 34)
        with self.assertRaises(TypeError):
            Rectangle(10, 20, "10", 34)
        with self.assertRaises(TypeError):
            Rectangle(10, 20, 10, "34")

    def test_area(self):
        """ tests Rectangle area """
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_str(self):
        """ tests Rectangle __str__method """
        r1 = Rectangle(4, 6, 2, 1, 12)
        str1 = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str1, str(r1))


if __name__ == "__main__":
    unittest.main()
