#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start
from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        edges = []
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    edges.append((i,j))
        

        parent = [i for i in range(n)]
        rank = [1] * n


        def find(n1):
            if parent[n1] == n1:
                return n1
            
            parent[n1] = find(parent[n1])
            return parent[n1]
            
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if rank[p2] > rank [p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]

            else:
                parent[p2] = p1
                rank[p1] += rank[p2]

            return 1
        
        result = n
        for n1, n2 in edges:
            result -= union(n1, n2)

        return result
        
# @lc code=end

