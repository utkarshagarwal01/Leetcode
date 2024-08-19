#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0]) 
        dp = [[-1]*n for _ in range(m)]

        def dfs(i,j):
            if i == m or j == n:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            bottom = dfs(i+1, j)
            right = dfs(i, j+1)
            bottomRight = dfs(i+1, j+1)

            res = 1 + min(bottom, right, bottomRight) if matrix[i][j] == "1" else 0
            

            dp[i][j] = res
            # print("for {0}:{1} = {2}".format(i,j,res))

            return res
        
        dfs(0,0)

        maxVal = max([ele for row in dp for ele in row])        
        # print(dp)
        # print(maxVal*maxVal)
        return maxVal*maxVal
    
s = Solution()
# s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
s.maximalSquare([["0","1"],["1","0"]])
# s.maximalSquare([["1","0","1","1"],["1","1","0","1"], ["1","1","1","1"]])
# @lc code=end