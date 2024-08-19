#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1, 1
        res = max(nums)
        
        for n in nums:
            if n == 0:
                curMax, curMin = 1, 1
            else:
                tmp = n * curMax
                curMax = max(tmp, n*curMin, n)
                curMin = min(tmp, n*curMin, n)

                res = max(res, curMax)

        return res
                 

# @lc code=end

