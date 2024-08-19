#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = [-1] * len(s)

        def isPossible(i):
            # print("Checking: {0}".format(i))
            if i >= len(s):
                return 1
            if memo[i] != -1:
                return memo[i]

            for j in range(i+1, len(s)+1):
                if (s[i:j] in wordSet) and isPossible(j):
                    memo[i] = 1
                    return memo[i]

            memo[i] = 0
            return memo[i]
        
        res = isPossible(0)

        # print(res, memo)
        return bool(res)

s = Solution()
print(s.wordBreak("leetcode", ["leet", "code"]))
# @lc code=end

