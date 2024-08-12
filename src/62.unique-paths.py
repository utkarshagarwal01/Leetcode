#
# @lc app=leetcode id=62 lang=python
#
# [62] Unique Paths
#

# @lc code=start
import math

class Solution(object):
    def ncr(self, n,r):
        
        numerator = math.factorial(n)
        numerator /= math.factorial(n-r)
        numerator /= math.factorial(r)
        
        return numerator 

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.ncr(m+n-2, m-1)

         
        
# @lc code=end

