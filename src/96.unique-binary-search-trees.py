#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        memo = [-1] * (n+1)
        memo[0], memo[1] = 1, 1

        def dfs(n):
            if memo[n] != -1:
                return memo[n]

            if n == 0 or n == 1:
                return 1

            count = 0
            for i in range(0, n):
                count += dfs(i) * dfs(n-i-1)

            memo[n] = count
            return count

        return dfs(n)

# s = Solution()
# print(s.numTrees(3))
# @lc code=end

