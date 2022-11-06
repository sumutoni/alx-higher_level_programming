#!/usr/bin/python3
"""unittest file for Base class"""
import unittest
import json
import sys
from io import StringIO
from unittest.mock import patch, call
sys.path.append('../..')
from models.square import Square
from models.base import Base

class TestRectangle(unittest.TestCase):
     """Test class for Base class"""

     def setUp(self):
        self.r1 = Square(1)
        self.r2 = Square(1, 2)
        self.r3 = Square(1, 2, 3)
        self.r = Square(1, 2, 3, 4)

     def tearDown(self):
         pass

     def test_values(self):
         self.assertEqual(self.r1.size, 1)
         self.assertEqual(self.r2.size, 1)
         self.assertEqual(self.r3.size, 1)
         self.assertEqual(self.r.size, 1)
         self.assertEqual(self.r.x, 2)
         self.assertEqual(self.r2.x, 2)
         self.assertEqual(self.r3.x, 2)
         self.assertEqual(self.r.y, 3)
         self.assertEqual(self.r3.y, 3)
         self.assertEqual(self.r.id, 4)

     def test_valueError(self):
         with self.assertRaises(ValueError):
             self.r4 = Square(0)

     def test_valEr(self):
         with self.assertRaises(ValueError):
             self.r5 = Square(2, -1)

     def test_valEr2(self):
         with self.assertRaises(ValueError):
             self.r6 = Square(2, 1, -4)

     def test_valEr3(self):
         with self.assertRaises(ValueError):
             self.r7 = Square(-1)

     def test_typeError(self):
         with self.assertRaises(TypeError):
             self.r8 = Square("2")

     def test_typeEr(self):
         with self.assertRaises(TypeError):
             self.r9 = Square(2, "7")

     def test_typeEr2(self):
         with self.assertRaises(TypeError):
             self.r10 = Square(2, 7, "8")

     def test_area(self):
         self.assertEqual(self.r1.area(), 1)
         self.assertEqual(self.r2.area(), 1)

     def test_update(self):
         rec = Square(4, 8, 9, 3)
         new = [5, 3, 6]
         rec.update(*new)
         self.assertEqual(rec.__str__(), "[Square] (5) 6/9 - 3")

     def test_display(self):
         rec = Square(3)
         expected = '###\n###\n###\n'
         with patch('sys.stdout', new = StringIO()) as fake:
             rec.display()
             self.assertEqual(fake.getvalue(), expected)

     def test_to_dictionary(self):
         rec = Square(2, 6, 8, 9)
         self.assertEqual(rec.to_dictionary(), {'id': 9, 'x': 6, 'y': 8,
                                                'size': 2})

     def test_create(self):
         dict_crea = {'id': 21}
         rec = Square.create(**dict_crea)
         self.assertEqual(type(rec), Square)
         self.assertEqual(rec.id, 21)

     def test_create2(self):
         dict_crea = {'id': 21, 'size': 4}
         rec = Square.create(**dict_crea)
         self.assertEqual(type(rec), Square)
         self.assertEqual(rec.id, 21)
         self.assertEqual(rec.size, 4)

     def test_create3(self):
         dict_crea = {'id': 21, 'size': 4, 'x': 3}
         rec = Square.create(**dict_crea)
         self.assertEqual(type(rec), Square)
         self.assertEqual(rec.id, 21)
         self.assertEqual(rec.size, 4)
         self.assertEqual(rec.x, 3)

     def test_create5(self):
         dict_crea = {'id': 21, 'size': 4, 'x': 3, 'y': 7}
         rec = Square.create(**dict_crea)
         self.assertEqual(type(rec), Square)
         self.assertEqual(rec.id, 21)
         self.assertEqual(rec.size, 4)
         self.assertEqual(rec.x, 3)
         self.assertEqual(rec.y, 7)

     def test_save_to_file1(self):
         obj = None
         Square.save_to_file(obj)
         filename = 'Square.json'
         with open(filename, "r", encoding="utf-8") as fil:
             self.assertEqual([], json.loads(fil.read()))

     def test_save_to_file2(self):
         Square.save_to_file([])
         filename = 'Square.json'
         with open(filename, "r", encoding="utf-8") as fil:
             self.assertEqual([], json.loads(fil.read()))

     def test_save_to_file3(self):
         Square.save_to_file([Square(1)])
         filename = 'Square.json'
         with open(filename, "r", encoding="utf-8") as fil:
             obj2 = json.loads(fil.read())
             for item in obj2:
                self.assertEqual(type(item), dict)

     def test_load_from_file1(self):
        recs = Base.load_from_file()
        self.assertEqual([], recs)

     def test_load_from_file2(self):
         recs = Square.load_from_file()
         for item in recs:
             self.assertEqual(type(item), Square)

if __name__ == '__main__':
    unittest.main()
