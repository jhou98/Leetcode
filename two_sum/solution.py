# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
class Solution:
    # This solution would be O(n)^2, which is not ideal
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            x = nums[i]
            y = target - x
            for j in range(i+1, len(nums)):
                if nums[j] == y: 
                    return [i, j]

    # This solution would take O(n) time, traversing list twice
    def twoSumV2(self, nums: List[int], target: int) -> List[int]:
        ndict = {} 
        for idx, val in enumerate(nums):
            ndict[val] = idx 
        for idx, val in enumerate(nums):
            y = target - val 
            if y in ndict and ndict[y] != idx: 
                return [idx, ndict[y]]        

    # This solution is also O(n) time, but only traverses the list once 
    def twoSumV2(self, nums: List[int], target: int) -> List[int]:
        ndict = {} 
        for idx, val in enumerate(nums):
            y = target - val 
            if y not in ndict: 
                ndict[val] = idx
            else: 
                return [idx,ndict[y]]