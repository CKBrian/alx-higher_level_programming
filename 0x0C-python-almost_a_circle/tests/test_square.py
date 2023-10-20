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
        self.assertEqual(print_res, "[Square] (23) 0/0 - 10\n")

        # Test of Square(2, 10) exists
        sr2 = Square(2, 10)
        output = StringIO()
        sys.stdout = output
        print(sr2)
        print_res = output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertEqual(print_res, "[Square] (24) 10/0 - 2\n")
        self.assertEqual(sr2.id, 24)

        # Test of Square(2, 10, 22) exists
        sr3 = Square(2, 10, 22)
        output = StringIO()
        sys.stdout = output
        print(sr3)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Square] (25) 10/22 - 2\n")
        self.assertEqual(sr3.id, 25)

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

    def test_display(self):
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

    def test_update(self):
        """ tests Square update method """
        r1 = Square(10, 10, 10, 10)

        r1.update(89)
        output = StringIO()
        sys.stdout = output
        print(r1)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Square] (89) 10/10 - 10\n")

        r1.update(89, 2)
        output = StringIO()
        sys.stdout = output
        print(r1)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Square] (89) 10/10 - 2\n")

        r1.update(89, 2, 3)
        output = StringIO()
        sys.stdout = output
        print(r1)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Square] (89) 3/10 - 2\n")

        r1.update(89, 2, 3, 4)
        output = StringIO()
        sys.stdout = output
        print(r1)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Square] (89) 3/4 - 2\n")

        r1.update(x=34, y=54)
        output = StringIO()
        sys.stdout = output
        print(r1)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Square] (89) 34/54 - 2\n")

        r1.update(size=7, id=809, y=1)
        output = StringIO()
        sys.stdout = output
        print(r1)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Square] (809) 34/1 - 7\n")

    def test_to_dictionary(self):
        """ tests Square to_dictionary method """
        sr1 = Square(10, 1, 9, 123)
        sr1_dict = sr1.to_dictionary()
        self.assertEqual(sr1_dict, {'x': 1, 'y': 9, 'id': 123, 'size': 10})

    def test_save_to_file(self):
        """ tests save_to_file class method """
        r1 = Rectangle(10, 2, 1, 9, 30)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        obj_list = [Rectangle.to_dictionary(rect) for rect in output]
        expected = [{'x': 1, 'y': 9, 'id': 30, 'height': 2, 'width': 10},
                    {'x': 0, 'y': 0, 'id': 26, 'height': 4, 'width': 2}]
        self.assertEqual(obj_list, expected)

        sr1 = Square(10, 1, 9, 31)
        sr2 = Square(2, 4)
        Square.save_to_file([sr1, sr2])
        output = Square.load_from_file()
        obj_list = [Square.to_dictionary(obj) for obj in output]
        expected = [{"id": 31, "size": 10, "x": 1, "y": 9},
                    {"id": 29, "size": 2, "x": 4, "y": 0}]
        self.assertEqual(obj_list, expected)


if __name__ == "__main__":
    unittest.main()
