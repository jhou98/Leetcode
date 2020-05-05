# Given a positive integer, output its complement number. 
# The complement strategy is to flip the bits of its binary representation.
# Ex.1- Input: 5, Output:2 
# Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

class Solution:
    def findComplement(self, num: int) -> int:
        """
        :type num: int
        :rtype: int
        """
        binary_num = f'{num:032b}'
        ind_start = (binary_num.find('1'))
        if ind_start is -1: return 1
        else: 
            x = 0
            mult = 1
            for i in range(31, ind_start-1, -1): 
                if binary_num[i] is '0':
                    x += mult
                mult *= 2
        return x
 


