#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniques = set()

        for n in nums:
            if n in uniques:
                return True
            uniques.add(n)

        return False 
# @lc code=end

