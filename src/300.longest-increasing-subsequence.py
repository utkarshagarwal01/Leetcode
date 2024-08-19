#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
from typing import List
from bisect import bisect_left
class Solution:
    def lengthOfLISNSquare(self, nums: List[int]) -> int:

        nums.insert(0, -100000)

        lisStartingAtI = [0] * len(nums)

        def LIS(i):
            if lisStartingAtI[i]:
                return lisStartingAtI[i]
            
            lisStartingAtI[i] = 1 + max([LIS(j) for j in range(i+1, len(nums)) if nums[j] > nums[i]], default=0)
            return lisStartingAtI[i]
        
        return LIS(0) -1
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [nums[0]]

        for x in nums[1:]:
            if x > lis[-1]:
                lis.append(x)
            else:
                pos = bisect_left(lis, x)
                lis[pos] = x
        
        return len(lis) 

s = Solution()
a = [10,9,2,5,3,7,101,18]
print(s.lengthOfLIS(a))
a = [0,1,0,3,2,3]
print(s.lengthOfLIS(a))
a = [7,7,7,7,7,7,7]
print(s.lengthOfLIS(a))

# @lc code=end

