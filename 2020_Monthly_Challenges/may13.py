# Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.
# Note:
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k == 0: 
            return num 
        elif k == len(num): 
            return "0"
        else: 
            # o/w we need to run our algorithm and remove numbers 
            # unsure about the algorithm 
            stack = []
            for i in range(len(num)):
                while stack and k > 0: 
                    if num[i] < stack[i]:
                        stack.pop()
                        k -= 1
                    stack.append(num[i])
                
