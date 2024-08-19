#
# @lc app=leetcode id=904 lang=python3
#
# [904] Fruit Into Baskets
#

# @lc code=start
from typing import List
from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = r = 0
        maxFruits = 0
        n = len(fruits)

        fruitMap = defaultdict(int)
        while r < n:
            if fruits[r] not in fruitMap and len(fruitMap) == 2:
                while len(fruitMap) != 1:
                    fruitMap[fruits[l]] -= 1
                    if not fruitMap[fruits[l]]:
                        del fruitMap[fruits[l]]
                    l += 1
            
            fruitMap[fruits[r]] += 1
            r += 1
            
            maxFruits = max(maxFruits, r-l)
        return maxFruits 
# @lc code=end

