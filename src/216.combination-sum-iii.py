#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        result = []

        numbers = list(range(1, 10))

        current = []

        def dfs(target, currentIndex):
            if target == 0 and len(current) == k:
                result.append(current.copy())
            elif target < 0 or k == len(current):
                return
            for i in range(currentIndex, 9):
                num = numbers[i]
                current.append(num)
                dfs(target - num, i + 1)
                current.pop()

        dfs(n, 0)
        return result
        
# @lc code=end

