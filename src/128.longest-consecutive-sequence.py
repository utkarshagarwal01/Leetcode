#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        q = 0
        while s:
            n = s.pop()
            l = n - 1
            while l in s:
                s.remove(l)
                l-=1
            h = n + 1
            while h in s:
                s.remove(h)
                h+=1
            q = max(q, h-l-1)
        return q
# @lc code=end

