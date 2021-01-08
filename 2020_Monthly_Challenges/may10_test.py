import unittest
from may10 import Solution

class testSolution(unittest.TestCase): 
    global sol
    sol = Solution()

    def test(self): 
        self.assertEqual(sol.findJudge(2,[[1,2]]), 2)
        self.assertEqual(sol.findJudge(3,[[1,3],[2,3]]), 3)

if __name__ == '__main__':
    unit_test = testSolution()
    unit_test.test()