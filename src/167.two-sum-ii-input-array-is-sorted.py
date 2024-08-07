#
# @lc app=leetcode id=167 lang=python
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(numbers) - 1

        while i<j:
            currSum = numbers[i] + numbers[j]
            if currSum == target:
                return [i+1, j+1]
            elif currSum<target:
                i+=1
            else:
                j-=1    
        
# @lc code=end

