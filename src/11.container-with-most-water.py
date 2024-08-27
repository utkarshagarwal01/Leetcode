#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxWater = 0
        while l < r:
            h1, h2 = height[l], height[r]
            currentWater = min(h1, h2) * (r-l)
            maxWater = max(maxWater, currentWater)

            if h1 < h2:
                l += 1
            else:
                r -= 1

        return maxWater
# @lc code=end

