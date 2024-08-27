#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        prefixProduct, postFixProduct = 1, 1

        for i, a in enumerate(nums):
            result[i] *= prefixProduct
            prefixProduct *= a
            result[n-i-1] *= postFixProduct
            postFixProduct *= nums[n-i-1]

        
        return result

# @lc code=end

