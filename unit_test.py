import application
import unittest

class FactorialTest(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(application.factorial(5), 120)
        self.assertEqual(application.factorial(1), 1)

    def test_minuscule(self):
        self.assertEqual(application.minuscule("Y"), "y")

if __name__ == '__main__':
    unittest.main()