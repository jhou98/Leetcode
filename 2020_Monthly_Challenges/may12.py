# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. 
# Find this single element that appears only once.

class Solution:
    def singleNonDuplicate(self, nums) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """        
        left = 0
        right = len(nums)-1
        while left < right: 
            mid = (left+right)//2
            if mid%2==0 and nums[mid] == nums[mid+1]:
                # if mid is even
                left = mid+2
            elif mid%2==1 and nums[mid] == nums[mid-1]:
                # if mid is odd
                left = mid+1
            else: 
                right = mid
        return nums[left]