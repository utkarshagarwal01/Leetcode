#
# @lc app=leetcode id=2055 lang=python3
#
# [2055] Plates Between Candles
#

# @lc code=start
from typing import List
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        # prefix_sum, left_candles, right_candles
        prefix_sum, left_candles, right_candles = [-1] * len(s), [-1] * len(s), [-1] * len(s)
        prefix_sum[0] = 1 if s[0] == '*' else 0
        left_candles[0] = -1 if s[0] == '*' else 0
        for i in range(1, len(s)):
            if s[i] == '*':
                prefix_sum[i] = prefix_sum[i-1] + 1
                left_candles[i] = left_candles[i-1]
            else:
                prefix_sum[i] = prefix_sum[i-1]
                left_candles[i] = i

        for i in range(len(s)-2, -1, -1):
            if s[i] == '|':
                right_candles[i] = i
            else:
                right_candles[i]= right_candles[i+1]

        print(prefix_sum, left_candles, right_candles)

        res = []
        for q in queries:
            x, y = q
            
            if right_candles[x] == -1 or left_candles[y] == -1:
                res.append(0)
            else:
                if prefix_sum[left_candles[y]] - prefix_sum[right_candles[x]] < 0:
                    res.append(0)
                else:    
                    res.append(prefix_sum[left_candles[y]] - prefix_sum[right_candles[x]])
        return res
# @lc code=end

