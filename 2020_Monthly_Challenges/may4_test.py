import unittest
from may4 import Solution

class testSolution(unittest.TestCase): 
    global sol
    sol = Solution()

    def test(self): 
        self.assertEqual(sol.findComplement(5),2)
        self.assertEqual(sol.findComplement(1),0)
        self.assertEqual(sol.findComplement(0),1)
        self.assertEqual(sol.findComplement(2147483647),0)

if __name__ == '__main__':
    unit_test = testSolution()
    unit_test.test()