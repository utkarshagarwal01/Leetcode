#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        current = []

        def dfs(open, close):
            if len(current) == 2*n:
                res.append("".join(current))
            else:
                if open < n:
                    current.append('(')
                    dfs(open + 1, close)
                    current.pop()
                if close < open:
                    current.append(')')
                    dfs(open, close +1 )
                    current.pop()
        dfs(0, 0)

        return res


# @lc code=end

