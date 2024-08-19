#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:

    def countSubstrings(self, s: str) -> int:
        c = 0
        
        for i in range(2*len(s) -1):
            l, r = i//2, i//2 
            if i%2 != 0:
                r += 1

            while l >=0 and r < len(s) and s[l] == s[r]:
                c +=1
                l -= 1
                r += 1

        return c
# @lc code=end

