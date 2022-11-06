#!/usr/bin/python3
"""unittest file for Base class"""
import unittest
import json
import sys
from io import StringIO
from unittest.mock import patch, call
sys.path.append('../..')
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
     """Test class for Base class"""

     def setUp(self):
        self.r1 = Rectangle(1, 2)
        self.r2 = Rectangle(1, 2, 3)
        self.r3 = Rectangle(1, 2, 3, 4)
        self.r = Rectangle(1, 2, 3, 4, 5)

     def tearDown(self):
         pass

     def test_values(self):
         self.assertEqual(self.r1.width, 1)
         self.assertEqual(self.r2.width, 1)
         self.assertEqual(self.r3.width, 1)
         self.assertEqual(self.r.width, 1)
         self.assertEqual(self.r.height, 2)
         self.assertEqual(self.r1.height, 2)
         self.assertEqual(self.r2.height, 2)
         self.assertEqual(self.r.x, 3)
         self.assertEqual(self.r2.x, 3)
         self.assertEqual(self.r3.x, 3)
         self.assertEqual(self.r.y, 4)
         self.assertEqual(self.r3.y, 4)
         self.assertEqual(self.r.id, 5)

     def test_valueError(self):
         with self.assertRaises(ValueError):
             self.r4 = Rectangle(0, 2)

     def test_valEr(self):
         with self.assertRaises(ValueError):
             self.r5 = Rectangle(2, 0)

     def test_valEr2(self):
         with self.assertRaises(ValueError):
             self.r6 = Rectangle(2, 1, -4)

     def test_valEr3(self):
         with self.assertRaises(ValueError):
             self.r7 = Rectangle(2, 1, 4, -3)

     def test_valEr4(self):
         with self.assertRaises(ValueError):
             self.r12 = Rectangle(-9, 3)

     def test_valEr5(self):
         with self.assertRaises(ValueError):
             self.r13 = Rectangle(7, -9)

     def test_typeError(self):
         with self.assertRaises(TypeError):
             self.r8 = Rectangle("2", 7)

     def test_typeEr(self):
         with self.assertRaises(TypeError):
             self.r9 = Rectangle(2, "7")

     def test_typeEr2(self):
         with self.assertRaises(TypeError):
             self.r10 = Rectangle(2, 7, "8")

     def test_typeEr3(self):
         with self.assertRaises(TypeError):
             self.r11 = Rectangle(2, 7, 8, "9")

     def test_area(self):
         self.assertEqual(self.r1.area(), 2)
         self.assertEqual(self.r2.area(), 2)

     def test_update(self):
         rec = Rectangle(4, 8, 9, 3)
         new = [5, 3, 6]
         rec.update(*new)
         self.assertEqual(rec.__str__(), "[Rectangle] (5) 9/3 - 3/6")

     def test_display(self):
         rec = Rectangle(3, 2)
         expected = '###\n###\n'
         with patch('sys.stdout', new = StringIO()) as fake:
             rec.display()
             self.assertEqual(fake.getvalue(), expected)

     def test_display1(self):
         rec = Rectangle(1, 2, 2)
         expected = '  #\n  #\n'
         with patch('sys.stdout', new = StringIO()) as fake:
             rec.display()
             self.assertEqual(fake.getvalue(), expected)

     def test_to_dictionary(self):
         rec = Rectangle(2, 6, 8, 9, 1)
         self.assertEqual(rec.to_dictionary(), {'id': 1, 'width': 2,
                                                'height': 6, 'x': 8, 'y': 9})

     def test_create(self):
         dict_crea = {'id': 21}
         rec = Rectangle.create(**dict_crea)
         self.assertEqual(type(rec), Rectangle)
         self.assertEqual(rec.id, 21)

     def test_create2(self):
         dict_crea = {'id': 21, 'width': 4}
         rec = Rectangle.create(**dict_crea)
         self.assertEqual(type(rec), Rectangle)
         self.assertEqual(rec.id, 21)
         self.assertEqual(rec.width, 4)

     def test_create3(self):
         dict_crea = {'id': 21, 'width': 4, 'height': 5}
         rec = Rectangle.create(**dict_crea)
         self.assertEqual(type(rec), Rectangle)
         self.assertEqual(rec.id, 21)
         self.assertEqual(rec.width, 4)
         self.assertEqual(rec.height, 5)

     def test_create4(self):
         dict_crea = {'id': 21, 'width': 4, 'height': 5, 'x': 3}
         rec = Rectangle.create(**dict_crea)
         self.assertEqual(type(rec), Rectangle)
         self.assertEqual(rec.id, 21)
         self.assertEqual(rec.width, 4)
         self.assertEqual(rec.height, 5)
         self.assertEqual(rec.x, 3)

     def test_create5(self):
         dict_crea = {'id': 21, 'width': 4, 'height': 5, 'x': 3, 'y': 7}
         rec = Rectangle.create(**dict_crea)
         self.assertEqual(type(rec), Rectangle)
         self.assertEqual(rec.id, 21)
         self.assertEqual(rec.width, 4)
         self.assertEqual(rec.height, 5)
         self.assertEqual(rec.x, 3)
         self.assertEqual(rec.y, 7)

     def test_save_to_file1(self):
         obj = None
         Rectangle.save_to_file(obj)
         filename = 'Rectangle.json'
         with open(filename, "r", encoding="utf-8") as fil:
             self.assertEqual([], json.loads(fil.read()))

     def test_save_to_file2(self):
         obj = []
         Rectangle.save_to_file(obj)
         filename = 'Rectangle.json'
         with open(filename, "r", encoding="utf-8") as fil:
             self.assertEqual([], json.loads(fil.read()))

     def test_save_to_file3(self):
         obj = [Rectangle(1, 2), Rectangle(1, 5, 7, 7)]
         Rectangle.save_to_file(obj)
         filename = 'Rectangle.json'
         with open(filename, "r", encoding="utf-8") as fil:
             obj2 = json.loads(fil.read())
             for item in obj2:
                self.assertEqual(type(item), dict)

     def test_load_from_file1(self):
        recs = Square.load_from_file()
        self.assertEqual([], recs)

     def test_load_from_file2(self):
         recs = Rectangle.load_from_file()
         for item in recs:
             self.assertEqual(type(item), Rectangle)

if __name__ == '__main__':
    unittest.main()
