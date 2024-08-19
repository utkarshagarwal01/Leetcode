#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        current = []
        def dfs(minI, target):
            if target == 0:
                result.append(current.copy())
            else:
                for i in range(minI, len(candidates)):
                    if target - candidates[i] >= 0:
                        current.append(candidates[i])
                        dfs(i, target - candidates[i])
                        current.pop()

        dfs(0, target)
        return result
# @lc code=end

