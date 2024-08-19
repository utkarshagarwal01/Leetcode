#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        current = []
        def dfs(i, target):
            if target == 0:
                result.append(current.copy())
                return

            if target < 0 or i == len(candidates):
                return

            current.append(candidates[i])
            dfs(i+1, target - candidates[i])
            current.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            dfs(i+1, target)

        dfs(0, target)
        return result
# @lc code=end

s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5], 8))