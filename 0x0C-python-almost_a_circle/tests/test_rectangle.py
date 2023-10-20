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
        self.assertEqual(print_res, "[Rectangle] (7) 0/0 - 10/2\n")

        # Test of Rectangle(2, 10, 2) exists
        r2 = Rectangle(2, 10, 2)
        output = StringIO()
        sys.stdout = output
        print(r2)
        print_res = output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertEqual(print_res, "[Rectangle] (8) 2/0 - 2/10\n")
        self.assertIsInstance(r2, Base)
        self.assertEqual(r2.id - r1.id, 1)

        # Test of Rectangle(2, 10, 2, 12) exists
        r3 = Rectangle(2, 10, 2, 12)
        output = StringIO()
        sys.stdout = output
        print(r3)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Rectangle] (9) 2/12 - 2/10\n")
        self.assertEqual(r3.id, 9)

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

    def test_diplay(self):
        """ tests Rectangle display method """
        # Tests Rectangle(3, 2, 0, 0, 23).display()
        output = StringIO()
        sys.stdout = output

        Rectangle(3, 2, 0, 0, 23).display()

        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "###\n###\n")

        # Tests Rectangle(3, 2, 2, 0, 24).display()
        output = StringIO()
        sys.stdout = output

        Rectangle(3, 2, 2, 0, 24).display()

        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "  ###\n  ###\n")

        # Tests Rectangle(3, 2, 0, 2, 25).display()
        output = StringIO()
        sys.stdout = output

        Rectangle(3, 2, 0, 2, 25).display()

        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "\n\n###\n###\n")

    def test_update(self):
        """ tests Rectangle update method """
        r1 = Rectangle(10, 10, 10, 10, 10)

        r1.update(89)
        output = StringIO()
        sys.stdout = output
        print(r1)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Rectangle] (89) 10/10 - 10/10\n")

        r1.update(89, 2)
        output = StringIO()
        sys.stdout = output
        print(r1)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Rectangle] (89) 10/10 - 2/10\n")

        r1.update(89, 2, 3)
        output = StringIO()
        sys.stdout = output
        print(r1)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Rectangle] (89) 10/10 - 2/3\n")

        r1.update(89, 2, 3, 4)
        output = StringIO()
        sys.stdout = output
        print(r1)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Rectangle] (89) 4/10 - 2/3\n")

        r1.update(89, 2, 3, 4, 5)
        output = StringIO()
        sys.stdout = output
        print(r1)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Rectangle] (89) 4/5 - 2/3\n")

    def test_to_dictionary(self):
        """ tests Rectangle to_dictionary method """
        r1 = Rectangle(10, 2, 1, 9, 123)
        r1_dict = r1.to_dictionary()
        self.assertEqual(r1_dict, {'x': 1, 'y': 9, 'id': 123, 'height': 2,
                                   'width': 10})

    def test_save_to_file(self):
        """ tests save_to_file class method """
        Rectangle.save_to_file(None)
        output = Rectangle.load_from_file()
        obj_list = [Rectangle.to_dictionary(rect) for rect in output]
        self.assertEqual(obj_list, [])

        Rectangle.save_to_file([])
        output = Rectangle.load_from_file()
        obj_list = [Rectangle.to_dictionary(rect) for rect in output]
        self.assertEqual(obj_list, [])

        r1 = Rectangle(10, 2, 1, 9, 30)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        obj_list = [Rectangle.to_dictionary(rect) for rect in output]
        expected = [{'x': 1, 'y': 9, 'id': 30, 'height': 2, 'width': 10},
                    {'x': 0, 'y': 0, 'id': 10, 'height': 4, 'width': 2}]
        self.assertEqual(obj_list, expected)

    def test_create(self):
        """ tests create class method """
        obj_dict = {'x': 1, 'y': 9, 'id': 130, 'height': 2, 'width': 10}
        r2 = Rectangle.create(**obj_dict)
        self.assertEqual(r2.to_dictionary(), obj_dict)


if __name__ == "__main__":
    unittest.main()
