#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
from math import ceil
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows < 3:
            cols = ceil(n/numRows)
        else:
            cols = ceil(len(s)/ (2*numRows -2)) * (numRows - 1)
        matrix = [[0] * cols for _ in range(numRows)]

        i, j = 0, 0
        for char in s:
            matrix[i][j] = char
            if i == 0 or matrix[i-1][j] != 0:
                i += 1
                if i == numRows:
                    i -= 2 if numRows != 1 else 1
                    j += 1
            else:
                i -= 1
                j += 1

        res = []
        for row in matrix:
            for ele in row:
                if ele != 0:
                    res.append(ele)

        return ("".join(res)) 

# @lc code=end

