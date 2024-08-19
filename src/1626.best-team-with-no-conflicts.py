#
# @lc app=leetcode id=1626 lang=python3
#
# [1626] Best Team With No Conflicts
#

# @lc code=start
from typing import List
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        ageScores = list(zip(ages, scores))
        ageScores.sort()

        scores = [s for a,s in ageScores]
        n = len(scores)
        memo = [0] * n

        def maxScore(i):
            if memo[i]:
                return memo[i]
            memo[i] = scores[i] + max([maxScore(j) for j in range(i+1, n) if scores[j] >= scores[i]], default=0)
            return memo[i]
        
        for i in range(n):
            maxScore(i)

        return max(memo)
    
# s = Solution()
# s.bestTeamScore([1,2,3,5], [8,9,10,1])
    
    # def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
    #     scoreAges = [(s,a) for s,a in zip(scores, ages)]
    #     scoreAges.sort()

    #     scoreAges.insert(0, (0, float('-inf')))
    #     n = len(scoreAges)

    #     memo = {}
    #     def maxScore(i,j):
    #         if j >= n or i >= n:
    #             return 0

    #         if (i,j) in memo:
    #             return memo[(i,j)]    
            
    #         if scoreAges[i][1] > scoreAges[j][1]:
    #             res = maxScore(i, j+1)
    #             memo[(i,j)] = res
    #             return res

    #         res = max(maxScore(i, j+1), scoreAges[j][0] + maxScore(j, j+1))
    #         memo[(i,j)] = res

    #         return res

    #     return maxScore(0, 1)

# @lc code=end

