import unittest
import maxconsecutiveones

class FindMaxConsecutiveOnes(unittest.TestCase):
    def test_solution_one(self):
        self.assertEqual(maxconsecutiveones.solution_one([1,1,0,1,1,1]), 3)

    def test_solution_two(self):
        self.assertEqual(maxconsecutiveones.solution_two([1,1,0,1,1,1]), 3)


if __name__ == '__main__':
    unittest.main()
