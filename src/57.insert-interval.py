#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start

from bisect import insort
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        insort(intervals, newInterval) 

        # print(intervals)
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            left, right = intervals[i]
            prevLeft, prevRight = merged[-1]
            if prevRight >= left:
                merged[-1][1] = max(right, prevRight)
            else:
                merged.append(intervals[i])
        # print(merged)

        return merged   

sol = Solution()
print(sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
# @lc code=end

