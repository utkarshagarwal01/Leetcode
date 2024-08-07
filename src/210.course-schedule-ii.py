#
# @lc app=leetcode id=210 lang=python
#
# [210] Course Schedule II
#

# @lc code=start
import heapq


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        preReq = {c:[] for c in range(numCourses)}
        for crs, pre in prerequisites:
            preReq[crs].append(pre)

        heapq()
        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)

            for pre in preReq[crs]:
                if not dfs(pre):
                    return False
                
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)

            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
            
        return output

# @lc code=end

