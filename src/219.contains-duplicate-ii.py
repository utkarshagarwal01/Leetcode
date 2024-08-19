#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
from typing import List
from collections import defaultdict
from bisect import bisect_left
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numToPos = defaultdict(list)

        for i, a in enumerate(nums):
            if a in numToPos:
                j = i - k
                pos = bisect_left(numToPos[a], j)
                if pos < len(numToPos[a]):
                    return True
                
            numToPos[a].append(i)

        return False

        #Faster solution with sliding window and HashSet
    
s = Solution()
s.containsNearbyDuplicate([1, 0, 1, 1], 1)
# @lc code=end

