import unittest
from may12 import Solution

class testSolution(unittest.TestCase): 
    global sol
    sol = Solution()

    def test(self): 
        self.assertEqual(sol.singleNonDuplicate([1,1,2,3,3,4,4,8,8]),2)
        self.assertEqual(sol.singleNonDuplicate([3,3,7,7,10,11,11]),10)
        self.assertEqual(sol.singleNonDuplicate([1]),1)

if __name__ == '__main__':
    unit_test = testSolution()
    unit_test.test()