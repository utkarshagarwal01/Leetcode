#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start

from typing import List
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # points.sort(key=lambda x: x[0]*x[0] + x[1]*x[1])
        # return points[:k]

        distances = [(x*x+y*y,x,y) for x,y in points]
        heapq.heapify(distances)

        result = []
        for _ in range(k):
            d, x, y = heapq.heappop(distances)
            result.append([x,y])
        return result
# @lc code=end
# sol = Solution()
# print(sol.kClosest([[3,3],[5,-1],[-2,4]], 2))
