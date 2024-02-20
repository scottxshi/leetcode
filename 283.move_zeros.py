#
# @lc app=leetcode id=283 lang=python3
# @lcpr version=30116
#
# [283] Move Zeroes
#

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         l = 0
#         for r in range(len(nums)):
#             if nums[r] != 0 and nums[l] == 0:
#                 nums[l] , nums[r] = nums[r] ,nums[l] 
#             if nums[l] != 0:
#                 l += 1    
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        anchor = 0
        for explorer in range(len(nums)):
            if nums[explorer] != 0:
                nums[anchor], nums[explorer] = nums[explorer], nums[anchor]
                anchor += 1    
    

