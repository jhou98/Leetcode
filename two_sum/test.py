import unittest
from solution import Solution

class test(unittest.TestCase): 
    global sol 
    sol = Solution()

    def test(self):
        self.assertEqual(sol.twoSum([2,7,11,15], 9), [0,1])
        self.assertEqual(sol.twoSum([3,2,4], 6), [1,2])

if __name__ == '__main__':
    unit_test = test()
    unit_test.test()