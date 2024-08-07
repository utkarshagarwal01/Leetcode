#
# @lc app=leetcode id=215 lang=python
#
# [215] Kth Largest Element in an Array
#

# @lc code=start

import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        nums = [i*-1 for i in nums]

        heapq.heapify(nums)

        while k > 1:
            heapq.heappop(nums)
            k -= 1
        
        return -1*heapq.heappop(nums)
# @lc code=end

