#!/usr/bin/python3
""" unittests for the base class """
from unittest import TestCase
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
import sys


class TestSquareClass(TestCase):
    def test_instantiation(self):
        """ tests instantiation and attributes """
        # Test of Square(10) exists
        output = StringIO()
        sys.stdout = output

        sr1 = Square(10)
        print(sr1)

        sys.stdout = sys.__stdout__
        print_res = output.getvalue()
        self.assertEqual(print_res, "[Square] (20) 0/0 - 10\n")

        # Test of Square(2, 10) exists
        sr2 = Square(2, 10)
        output = StringIO()
        sys.stdout = output
        print(sr2)
        print_res = output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertEqual(print_res, "[Square] (21) 10/0 - 2\n")
        self.assertEqual(sr2.id, 21)

        # Test of Square(2, 10, 22) exists
        sr3 = Square(2, 10, 22)
        output = StringIO()
        sys.stdout = output
        print(sr3)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Square] (22) 10/22 - 2\n")
        self.assertEqual(sr3.id, 22)

        # Test of Square(2, 10, 2, 12) exists
        r4 = Square(2, 10, 2, 212)
        self.assertEqual(r4.id, 212)
        self.assertTrue(issubclass(Square, Rectangle))

    def test_values(self):
        """ ensures exceptions are raised approproately"""
        with self.assertRaises(TypeError):
            Square("10")
        with self.assertRaises(TypeError):
            Square()
        with self.assertRaises(ValueError):
            Square(-10)
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(ValueError):
            Square(10, 20, -34)
        with self.assertRaises(ValueError):
            Square(10, -10, 34)
        with self.assertRaises(TypeError):
            Square(10, "10", 34)
        with self.assertRaises(TypeError):
            Square(10, 10, "34")

    def test_area(self):
        """ tests Square area """
        sr1 = Square(3)
        self.assertEqual(sr1.area(), 9)
        sr3 = Square(8, 0, 0, 212)
        self.assertEqual(sr3.area(), 64)

    def test_str(self):
        """ tests Square __str__method """
        sr1 = Square(4, 6, 2, 212)
        str1 = "[Square] (212) 6/2 - 4"
        self.assertEqual(str1, str(sr1))

    def test_str(self):
        """ tests Square display method """
        # Tests Square(2).display()
        output = StringIO()
        sys.stdout = output

        Square(2).display()

        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "##\n##\n")

        # Tests Square(2, 2).display()
        output = StringIO()
        sys.stdout = output

        Square(2, 2).display()

        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "  ##\n  ##\n")

        # Tests Square(2, 0, 2).display()
        output = StringIO()
        sys.stdout = output

        Square(2, 0, 2).display()

        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "\n\n##\n##\n")


if __name__ == "__main__":
    unittest.main()
