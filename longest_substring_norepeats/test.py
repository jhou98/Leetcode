import unittest
from solution import Solution

class test(unittest.TestCase): 
    global sol 
    sol = Solution()

    def test(self):
        self.assertEqual(sol.lengthOfLongestSubstring("bbbbb"),1)
        self.assertEqual(sol.lengthOfLongestSubstring(" "),1)
        self.assertEqual(sol.lengthOfLongestSubstring("dvdf"),3)
        self.assertEqual(sol.lengthOfLongestSubstring("abcabcdba"),4)

if __name__ == '__main__':
    unit_test = test()
    unit_test.test()