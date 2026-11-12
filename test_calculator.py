import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######## Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(0,0), 0)
        self.assertEqual(add(1232, -232), 1000)
        self.assertAlmostEqual(add(123.8, 5.556), 129.356)
        self.assertAlmostEqual(add(108.2, 7.99), 116.19)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(125, -1), 126)
        self.assertAlmostEqual(subtract(123.8, 5.556), 118.244)
        self.assertAlmostEqual(subtract(108.2, 7.99), 100.21)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 2), 4)
        self.assertEqual(mul(-234, 4), -936)
        self.assertAlmostEqual(mul(3.142, 7.5), 23.565)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(16, 2), 8)
        self.assertEqual(div(-9, 0.5), -18)
        self.assertAlmostEqual(div(261, 5), 52.2)


    ####### Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)


    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(2, 20), 4.3219281)
        self.assertAlmostEqual(logarithm(2, 10), 3.3219281)
        self.assertEqual(logarithm(10, 10), 1)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(1, 5)
    ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(13, 15), 19.849433241279207)


    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
           square_root(-2)
        self.assertEqual(square_root(25), 5)
        self.assertAlmostEqual(square_root(27), 5.196152422706631)


    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
