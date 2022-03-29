#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
python -m unittest [test_module]
python -m unittest test_module1 test_module2
python -m unittest test_module.TestClass
python -m unittest test_module.TestClass.test_method
python -m unittest discover -s project_directory -p "*test.py"

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

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    def setUp(self):
        print('Start testing')

    def tearDown(self):
        print('End test\n')

    def test_normal_output(self):
        m, n = 5, 10
        r_odd = parity(m)
        r_even = parity(n)
        print('Test normal output')
        self.assertEqual(r_odd, f'{m} is odd')
        self.assertEqual(r_even, f'{n} is even')

    def test_invalid_input(self):
        data_text = 'abc'
        r = parity(data_text)
        print('Test invalid input')
        self.assertIn('Invalid', r)

    @unittest.skip('Always skip')
    # @unittest.skipIf(2 > 1, 'Skip if the condition is true.')
    # @unittest.skipUnless(2 < 1, 'Skip unless the condition is true.')
    def test_argerror(self):
        arg1, arg2 = 5, 10
        print('Test wrong parameter')
        with self.assertRaises(TypeError):
            parity(arg1, arg2)

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')


if __name__ == '__main__':
    # unittest.main()
    testcase = unittest.TestLoader().loadTestsFromTestCase(TestParity)
    # testcase = unittest.TestLoader().loadTestsFromName('my_unittest2.Test2.test2_1')
    disc_test = unittest.TestLoader().discover('.', '*test2.py')
    suite = unittest.TestSuite([testcase, disc_test])
    suite.addTest(TestParity('test_argerror'))
    # 可运行test case或test suite
    unittest.TextTestRunner(verbosity=2).run(suite)