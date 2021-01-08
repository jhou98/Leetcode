import unittest
from may8 import Solution

class testSolution(unittest.TestCase):
    global sol 
    sol = Solution()

    def test(self):
        self.assertEqual(sol.checkStraightLine([[1,1],[2,2]]), True)
        self.assertEqual(sol.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]), True)
        self.assertEqual(sol.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]), False)

if __name__ == '__main__':
    unit_test = testSolution()
    unit_test.test()
