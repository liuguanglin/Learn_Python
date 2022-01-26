#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
python -m unittest my_unittest
python -m unittest test_module1 test_module2
python -m unittest test_module.TestClass
python -m unittest test_module.TestClass.test_method

Method
assertEqual(a, b)
assertNotEqual(a, b)
assertTrue(x)
assertFalse(x)
assertIs(a, b)
assertIsNot(a, b)
assertIsNone(x)
assertIsNotNone(x)
assertIn(a, b)
assertNotIn(a, b)
assertIsInstance(a, b)
assertNotIsInstance(a, b)
"""

import unittest
from test_demo import parity


class TestParity(unittest.TestCase):
    def setUp(self):
        print('Start testing')

    def tearDown(self):
        print('End test')

    def test_normal_output(self):
        m, n = 5, 10
        r_odd = parity(m)
        r_even = parity(n)
        self.assertEqual(r_odd, f'{m} is odd')
        self.assertEqual(r_even, f'{n} is even')

    def test_invalid_input(self):
        data_text = 'abc'
        r = parity(data_text)
        self.assertIn('Invalid', r)

    def test_argerror(self):
        arg1, arg2 = 5, 10
        with self.assertRaises(TypeError):
            parity(arg1, arg2)


if __name__ == '__main__':
    unittest.main()
