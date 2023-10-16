#!/usr/bin/python3
""" unittests for the base class """
from unittest import TestCase
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleClass(TestCase):
    def test_attributes(self):
        """ tests attributes """

        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

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
