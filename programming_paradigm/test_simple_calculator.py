import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
       
        self.assertEqual(self.calc.add(2, 3), 5)
        

    def test_subtraction(self):
        
        self.assertEqual(self.calc.subtract(-5, -7), 2)

    def test_multiplication(self):
        
        self.assertEqual(self.calc.multiply(-5, -7), 35)

    def test_division(self):
    
        self.assertEqual(self.calc.divide(-9, -3), 3)

    def test_division_by_zero(self):
       
        self.assertIsNone(self.calc.divide(0, 0))

if __name__ == '__main__':
    unittest.main()
