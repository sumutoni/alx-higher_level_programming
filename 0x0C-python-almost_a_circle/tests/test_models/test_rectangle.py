#!/usr/bin/python3
"""unittest file for Base class"""
import unittest
import sys
sys.path.append('../..')
from models.rectangle import Rectangle


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
         seld.assertEqual(self.r.height, 2)
         self.assertEqual(self.r1.height, 2)
         self.assertEqual(self.r2.height, 2)
         self.assertEqual(self.r.x, 3)
         self.assertEqual(self.r2.x, 3)
         self.assertEqual(self.r3.x, 3)
         self.assertEqual(self.r.y, 4)
         self.assertEqual(self.r3.y, 4)
         self.assertEqual(self.r.id, 5)
         with self.assertRaises(ValueError):
             self.r4 = Rectangle(0, 2)
             self.r5 = Rectangle(2, 0)
             self.r6 = Rectangle(2, 1, -4)
             self.r7 = Rectangle(2, 1, 4, -3)
             self.r12 = Rectangle(-9, 3)
             self.r13 = Rectangle(-7, 9)

         with self.assertRaises(TypeError):
             self.r8 = Rectangle("2", 7)
             self.r9 = Rectangle(2, "7")
             self.r10 = Rectangle(2, 7, "8")
             self.r11 = Rectangle(2, 7, 8, "9")

     def test_area(self):
         self.assertEqual(self.r1.area(), 2)
         self.assertEqual(self.r2.area(), 2)

     def test_update(self):
         rec = Rectangle(4, 8, 9, 3)
         new = [5, 3, 6]
         rec.update(*new)
         self.assertEqual(rec.__str__(), "[Rectangle] (5) 9/3 - 3/6")

if __name__ == '__main__':
    unittest.main()
