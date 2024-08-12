#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
from typing import *
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        nums.sort()
        n = len(nums)
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue

            #2SUM

            l, r = i+1, n-1
            while l < r:
                target = a + nums[l] + nums[r]
                if target > 0:
                    r -= 1
                elif target < 0:
                    l += 1
                else:
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1

        return result
                    
# @lc code=end

