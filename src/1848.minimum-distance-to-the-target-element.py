#
# @lc app=leetcode id=1848 lang=python3
#
# [1848] Minimum Distance to the Target Element
#

# @lc code=start
from typing import List
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        l = r = start
        while l >= 0 or r < len(nums):
            if l >= 0 and nums[l] == target: return start - l
            if r < len(nums) and nums[r] == target: return r - start
            l -= 1
            r += 1

# @lc code=end

