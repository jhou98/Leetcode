import unittest
from may5 import Solution

class testSolution(unittest.TestCase): 
    global sol
    sol = Solution()

    def test(self): 
        self.assertEqual(sol.firstUniqChar("leetcode"),0)
        self.assertEqual(sol.firstUniqChar("loveleetcode"),2)     
        self.assertEqual(sol.firstUniqChar(""),-1)
        self.assertEqual(sol.firstUniqChar("lloo"),-1)
        self.assertEqual(sol.firstUniqChar("aabbccddeeffg"),12)    

if __name__ == '__main__':
    unit_test = testSolution()
    unit_test.test()