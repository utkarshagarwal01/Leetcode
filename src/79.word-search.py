#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        wordLen = len(word)

        visiting = set()
        def dfs(r, c, i):
            if i == wordLen:
                return True
            
            if (r, c) in visiting or \
                r < 0 or c < 0 or r == m or c == n or \
                board[r][c] != word[i]:
                return False
            
            visiting.add((r, c))

            left =  dfs(r, c - 1, i + 1)
            right = dfs(r, c + 1, i + 1)
            up =    dfs(r - 1, c, i + 1)
            down =  dfs(r + 1, c, i + 1)
            
            possible = left or right or up or down 
            
            visiting.remove((r, c))
            return possible

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
                
        return False
# @lc code=end

