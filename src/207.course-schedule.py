#
# @lc app=leetcode id=207 lang=python
#
# [207] Course Schedule
#

# @lc code=start
class Solution(object):




    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = {c:[] for c in range(numCourses)}

        for crs, pre in prerequisites:
            graph[crs].append(pre)


        visiting = set()

        def dfs(node):
            if node in visiting:
                return False
            
            if not graph[node]:
                return True 
            visiting.add(node)

            for preq in graph[node]:
                if not dfs(preq):
                    return False

            graph[node] = []
            visiting.remove(node)
            return True 

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

    
        


# @lc code=end

