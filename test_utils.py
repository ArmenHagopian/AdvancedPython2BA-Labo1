# test_utils.py
# Author: Sébastien Combéfis
# Version: February 2, 2016

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        with self.assertRaises(ValueError):
            utils.fact(-1)
        self.assertEqual(utils.fact(0), 1)
        self.assertEqual(utils.fact(1), 1)
        self.assertEqual(utils.fact(2), 2)
        # À compléter...
        pass
    
    def test_roots(self):
        self.assertEqual(utils.roots(0, 0, 0), (0))
        self.assertEqual(utils.roots(1, 0, 1), ())

        # À compléter...
        pass
    
    def test_integrate(self):
        # À compléter...
        self.assertEqual(utils.integrate('x ** 2 - 1', -1, 1), -4.0/3)
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())