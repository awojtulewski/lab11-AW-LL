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

    # ####### Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code
    #
    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ####### Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)


    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(log(2, 20), 4.3219281)
        self.assertAlmostEqual(log(2, 10), 3.3219281)
        self.assertEqual(log(10, 10), 1)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            log(1, 5)
    ##########################
    
    # ####### Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code
    #
    # def test_hypotenuse(self): # 3 assertions
    #     fill in code
    #
    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    # #########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()