import unittest
from may6 import Solution

class testSolution(unittest.TestCase): 
    global sol
    sol = Solution()

    def test(self): 
        self.assertEqual(sol.majorityElement([3,2,3]),3)
        self.assertEqual(sol.majorityElement([2,2,2,1,2,1]),2)
        self.assertEqual(sol.majorityElement([1]),1)


if __name__ == '__main__':
    unit_test = testSolution()
    unit_test.test()