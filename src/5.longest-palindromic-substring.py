#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLength = 0
        indices = None

        for i in range(2*len(s) - 1):
            l, r = (i//2, i//2) if i % 2 == 0 else (i//2, i//2 + 1)

            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            # print(i, r - l - 1)

            if r - l - 1 > maxLength:
                indices = (l+1, r-1)
                maxLength = r - l - 1
        
        return s[indices[0]:indices[1] + 1]
                


# @lc code=end

