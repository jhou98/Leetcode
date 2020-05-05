import unittest
from may2 import Solution

class testSolution(unittest.TestCase): 
    global sol
    sol = Solution()

    def test(self): 
        self.assertEqual(sol.numJewelsInStones('aA','aAAbbbb'), 3)
        self.assertEqual(sol.numJewelsInStones('z','ZZ'), 0)
        self.assertEqual(sol.numJewelsInStones('','A'),0)
        self.assertEqual(sol.numJewelsInStones('A',''),0)
        self.assertEqual(sol.numJewelsInStones('',''),0)
        self.assertEqual(sol.numJewelsInStones('',''),0)
        self.assertEqual(sol.numJewelsInStones('z','aaaaaaaaaaz'),1)
        self.assertEqual(sol.numJewelsInStones('x','xzzzzzzzzzzzz'),1)
        self.assertEqual(sol.numJewelsInStones('ebd','bbb'),3)

if __name__ == '__main__':
    unit_test = testSolution()
    unit_test.test()