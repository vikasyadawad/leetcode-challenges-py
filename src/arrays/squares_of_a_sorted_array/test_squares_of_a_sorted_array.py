import unittest
import squares_of_a_sorted_array

class MyTestCase(unittest.TestCase):
    def test_solution_one(self):
        self.assertEqual(squares_of_a_sorted_array.solution_one([-4,-1,0,3,10]), [0,1,9,16,100])
        self.assertEqual(squares_of_a_sorted_array.solution_one([-7,-3,2,3,11]), [4,9,9,49,121])


if __name__ == '__main__':
    unittest.main()
