#!/usr/bin/python3
""" unittests for the base class """
from unittest import TestCase
from models.base import Base


class TestBaseClass(TestCase):
    def test_id(self):
        """ tests attributes """
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base(3)
        self.assertEqual(b5.id, 3)

        b5 = Base()
        self.assertEqual(b5.id, 4)


if __name__ == "__main__":
    unittest.main()
