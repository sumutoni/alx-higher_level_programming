#!/usr/bin/python3
"""unittest file for Base class"""
import unittest
import sys
sys.path.append('../..')
from models.base import Base


class TestBase(unittest.TestCase):
     """Test class for Base class"""

     def setUp(self):
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(87)
        self.b4 = Base()

     def tearDown(self):
         pass

     def test_ids(self):
         self.assertEqual(self.b1.id, 1)
         self.assertEqual(self.b2.id, 2)
         self.assertEqual(self.b3.id, 87)
         self.assertEqual(self.b4.id, 3)

     def test_to_json_string(self):
         dictn = {'id': 12}
         li = [dictn]
         json_str = Base.to_json_string(li)
         self.assertEqual(json_str, '[{"id": 12}]')

     def test_json_string(self):
         li = Base.from_json_string('[{"id": 90}]')
         self.assertEqual([{'id': 90}], li)

if __name__ == '__main__':
    unittest.main()
