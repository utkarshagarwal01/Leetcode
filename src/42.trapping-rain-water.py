#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        temp = 0
        lMax = []
        for h in height:
            temp = max(temp, h)
            lMax.append(temp)

        temp = 0
        rMax = []
        for h in reversed(height):
            temp = max(temp, h)
            rMax.append(temp)

        rMax = list(reversed(rMax))
        # print(lMax, "\n", rMax)

        count = 0

        for i in range(len(height)):
            count +=  min(lMax[i],rMax[i]) - height[i] 

        return count

s = Solution()
s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
# @lc code=end

