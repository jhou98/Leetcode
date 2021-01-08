# Given a positive integer num, write a function which returns True if num is a perfect square else False.
# Note: Do not use any built-in library function such as sqrt.
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        :type num: int
        :rtype: bool
        """
        if num is 1: 
            return True 
        else: 
            left = 2 
            right = num 
            while(left <= right):
                mid = (left + right)//2
                squared = mid * mid 
                if squared == num: 
                    return True 
                elif squared < num:
                    left = mid + 1
                elif squared > num: 
                    right = mid - 1
            return False   