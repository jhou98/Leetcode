import unittest
from may9 import Solution

class testSolution(unittest.TestCase):
    global sol 
    sol = Solution()

    def test(self):
        self.assertEqual(sol.isPerfectSquare(1),True)
        self.assertEqual(sol.isPerfectSquare(2),False)
        self.assertEqual(sol.isPerfectSquare(4),True)
        self.assertEqual(sol.isPerfectSquare(25),True)
        self.assertEqual(sol.isPerfectSquare(27),False)

if __name__ == '__main__':
    unit_test = testSolution()
    unit_test.test() 


