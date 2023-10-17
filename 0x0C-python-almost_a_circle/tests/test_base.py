#!/usr/bin/python3
""" unittests for the base class """
from unittest import TestCase
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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

    def test_to_json_string(self):
        """ tests to_json_string static method """
        json_str = Base.to_json_string(None) #exists
        self.assertEqual("[]", json_str)

        json_str = Base.to_json_string([]) #exists
        self.assertEqual("[]", json_str)

        json_str = Base.to_json_string([ {'id': 12} ]) #returning a string exists
        self.assertIsInstance(json_str, str)
        self.assertEqual('[{"id": 12}]', json_str)

    def test_from_json_string(self):
        """ tests from_json_string static method """
        json_list = Base.from_json_string(None) #exists
        self.assertEqual([], json_list)

        json_list = Base.from_json_string("[]") #exists
        self.assertEqual([], json_list)

        json_list = Base.from_json_string('[{ "id": 89 }]') #exists
        self.assertEqual([{ 'id': 89 }], json_list)


if __name__ == "__main__":
    unittest.main()
