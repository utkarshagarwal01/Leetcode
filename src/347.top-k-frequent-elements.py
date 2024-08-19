#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        buckets = [[] for i in range(len(nums) + 1)] 

        for val, count in counts.items():
            buckets[count].append(val)

        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
s = Solution()
print(s.topKFrequent([3,0,1,0], 1))
# @lc code=end

