# Given a string, find the first non-repeating character in it and return it's index. 
# If it doesn't exist, return -1.
# Ex 1: s = 'leetcode' , return 0
# Ex 2: s = 'loveleetcode' , return 2
import collections 

class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        s_count = collections.Counter(s)
        for idx, val in enumerate(s): 
            if s_count[val] == 1: 
                return idx 
        return -1
