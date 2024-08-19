#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP, minPrice = 0, prices[0]

        for price in prices[1:]:
            if price < minPrice:
                minPrice = price
            if maxP < (price - minPrice):
                maxP = price - minPrice
        
        return maxP
# @lc code=end

