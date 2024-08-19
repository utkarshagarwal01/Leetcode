#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#

# @lc code=start
from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(0, n+1)]
        rank = [1] * (n+1)

        def find(node):

            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]

            return node
        
        def union(n1, n2):
            uP1, uP2 = find(n1), find(n2)


            if uP1 == uP2:
                return 0
            
            if rank[uP1] > rank[uP2]:
                parent[uP2] = uP1
                rank[uP1] += rank[uP2]
            else:
                parent[uP1] = uP2
                rank[uP2] += rank[uP1]
        
            return 1
        
        for a,b in edges:
            if not union(a, b):
                return [a, b]
            
        

# @lc code=end

