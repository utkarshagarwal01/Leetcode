#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        charSet = set()
        l,r,n = 0,0,len(s)
        res = 0

        while r<n:
            if s[r] not in charSet:
                charSet.add(s[r])
                r += 1
                res = max(res, len(charSet))
            else:
                charSet.remove(s[l])
                l += 1
        return res
        
# @lc code=end

