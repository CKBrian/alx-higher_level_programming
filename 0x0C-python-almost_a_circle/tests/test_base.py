#!/usr/bin/python3
""" unittests for the base class """
from unittest import TestCase
from models.base import Base


class TestBaseClass(TestCase):
    def test_id(self):
        """ tests attributes """
        b1 = Base()
        B1 = Base()
        self.assertEqual(1, B1.id - b1.id)

        b2 = Base()
        b3 = Base()
        self.assertEqual(b3.id - b2.id, 1)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base(3)
        self.assertEqual(b5.id, 3)


if __name__ == "__main__":
    unittest.main()
