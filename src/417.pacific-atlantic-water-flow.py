#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
from typing import List
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, visit, prevHight):
            if (r,c) in visit or \
                r < 0 or c < 0 or r == m or c == n or \
                heights[r][c] < prevHight:
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(n):
            dfs(0, c, pacific, heights[0][c])
            dfs(m-1, c, atlantic, heights[m-1][c])

        for r in range(m):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, n-1, atlantic, heights[r][n-1])

        res = list(pacific & atlantic)
        res.sort()
        return res
# @lc code=end

