import unittest
import findevennumberofdigits

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(findevennumberofdigits.solution_one([12, 345, 2, 6, 7896]), 2)


if __name__ == '__main__':
    unittest.main()
