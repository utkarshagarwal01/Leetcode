#
# @lc app=leetcode id=77 lang=python
#
# [77] Combinations
#

# @lc code=start
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []

        def fillArray(arr, lastVal, currentPos):
            if currentPos == k:
                result.append(arr[:])
                return
            
            for i in range(lastVal+1, n+1):
                arr.append(i)
                fillArray(arr, i, currentPos+1)
                arr.pop()

        fillArray([], 0, 0)

        # return list(itertools.combinations([i for i in range(n+1), k]))

        return result
        
# @lc code=end

